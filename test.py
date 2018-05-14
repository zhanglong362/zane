#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import time
import json
import struct
import socket
import urllib
import hashlib
import logging
import MySQLdb
import requests
import threading


class UcloudBandwidth():
    def __init__(self):
        self.sms_server = '106.75.51.26'
        self.sms_port = 45678
        self.sms_users = ["operation"]  # operation: zhanglong
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s  %(filename)s[line:%(lineno)d]:%(levelname)s:%(message)s',
                            datefmt='%Y-%b-%d,%H:%M:%S',
                            filename='check-eip-bandwidth-c.log',
                            filemode='w')
        logging.getLogger("requests").setLevel(logging.WARNING)
        self.PublicKey = "ucloudzhanglong@gotye.com.cn1451271295000574312241"
        self.PrivateKey = "882a7eddf37eb59b62e16d7f0bdcf77cf825bf00"
        self.Password = "R290eWUuMzY1"
        self.ProjectId = "org-1164"
        self.Url = "http://api.ucloud.cn"
        self.region_bj1 = "cn-bj1"
        self.region_bj2 = "cn-bj2"
        self.region_hk = "hk"
        self.zone_A = "cn-bj1-01"
        self.zone_C = "cn-bj2-03"
        self.zone_HK = "hk-01"
        self.api_DescribeEIP = "DescribeEIP"
        self.api_DescribeShareBandwidth = "DescribeShareBandwidth"
        self.api_GetMetricOverview = "GetMetricOverview"
        self.api_DescribeBandwidthPackage = "DescribeBandwidthPackage"
        self.api_CreateBandwidthPackage = "CreateBandwidthPackage"
        self.log_normal = "C区 %s-%s 带宽监控正常 %s%% %sKB/s %sM "
        self.log_api_fail = "C区 Ucloud EIP 监控接口调用失败，发送短信报警 error api: "
        self.log_api_recovery = "C区 Ucloud EIP 监控接口调用恢复正常，发送短信报 error api: "
        self.log_buy_package = "C区 %s-%s 当前带宽%sM，已购买%sM%s小时带宽包，购买后带宽%sM，发送短信报警"
        self.log_buy_package_fail = "C区 %s-%s 当前带宽%sM，购买%sM%s小时带宽包失败，发送报警短"
        self.log_no_buy_package = "C区 %s-%s 第%s次带宽超阈值，使用率%s%% 带宽速度%s，当前带宽%sM，已超过%sM不再购买带宽包"
        self.log_share_eip_check = "C区 共享带宽 %s-%s 使用率%s%% 带宽速度%s，当前带宽%sM"
        self.log_keep_check = "C区 %s-%s 第%s次带宽超阈值，使用率%s%% 带宽速度%s，当前带宽%sM，不发短信报警，持续监控"
        self.log_eip_dict_null = "\033[31mC区 DescribeEIP 无此EIP %s\033[0m"
        self.log_eip_use_dict_null = "\033[31mC区 GetMetricOverview 无此EIP %s\033[0m"
        self.sms_api_fail = "C区 Ucloud EIP 监控接口调用失败，请查看"
        self.sms_api_recovery = "C区 Ucloud EIP 监控接口调用恢复正常"
        self.sms_buy_package = "C区 %s-%s 当前带宽%sM，已购买%sM%s小时带宽包，购买后带宽%sM"
        self.sms_buy_package_fail = "C区 %s-%s 当前带宽%sM，购买%sM%s小时带宽包失败，请查看"
        self.sms_no_buy_package = "C区 %s-%s 带宽超阈值，使用率%s%% 带宽速度%s，基础带宽%sM，当前带宽%sM，已超过50M不再购买带宽包"
        self.alert_bindwidth = 100
        self.interval = 30
        self.interval_buy_wait = 90

    def get_phone_list(self):
        conn = MySQLdb.connect(host="10.6.19.143", user="root", passwd="gotye2013", db="gotye_deploy",
                               charset="utf8")
        cursor = conn.cursor()

        phone_list = []
        for remark in self.sms_users:
            cursor.execute("select `phone_list` from `tbl_phone_list` where `remark`='%s'" % remark)
            for phone in cursor.fetchall():
                phone_list.append(phone[0])
        conn.close()
        logging.debug("phone_list: %s" % phone_list)
        return phone_list

    def send_sms(self, text):
        text = str(text)
        logging.debug("%s SMS text: %s" % (type(text), text))
        phone_list = self.get_phone_list()
        address = (self.sms_server, self.sms_port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)

        ntext = str(chr(len(text)) + text)
        msglen = len(ntext) + 4 + 12
        strc_format = str('<cHHI12s' + str(len(ntext)) + 's')

        for phone in phone_list:
            nphone = str(chr(len(phone)) + phone)
            msgcontant = struct.pack(strc_format, '0', msglen, 4, 0, nphone, ntext)
            s.send(msgcontant)
        s.close()

    def do_request(self, api_params):
        if api_params["Region"] == "cn-bj1":
            region = "A"
        elif api_params["Region"] == "cn-bj2":
            region = "C"
        api = api_params['Action']
        items = api_params.items()
        items.sort()
        params_data = ""
        for (k, v) in items:
            params_data += str(k) + str(v)
        params_data = params_data + self.PrivateKey
        sign = hashlib.sha1()
        sign.update(params_data)
        signature = sign.hexdigest()

        api_params["Signature"] = signature
        api_params = sorted(api_params.items(), key=lambda api_params: api_params[0])
        url = self.Url + "/?" + urllib.urlencode(api_params)

        try:
            r = requests.get(url)
        except Exception as e:
            logging.error("\033[31mHTTP ERROR%s\033[0m" % str(e))
            return
        try:
            r = json.loads(r.text)
        except:
            logging.error("\033[31m%s to Json failed:\033[0m %s" % (api, r.text))
        if r['RetCode'] != 0:
            logging.error("\033[31mRegion %s %s failed:\033[0m %s" % (region, api, r))
        logging.debug("\033[32mRegion %s %s success:\033[0m %s" % (region, api, r['RetCode']))
        return r

    def DescribeEIP(self):
        api_params = {
            "Action": self.api_DescribeEIP,
            "PublicKey": self.PublicKey,
            "ProjectId": self.ProjectId,
            "Region": self.region,
            "Offset": 0,
            "Limit": 200
        }
        r = self.do_request(api_params)
        if not r:
            return -1
        eip_dict = {}
        if not r.has_key("EIPSet"):
            return eip_dict
        for i in r['EIPSet']:
            if not i['Status'] == "used":
                continue
            eip = i['EIPAddr'][0]['IP']
            eip_id = i['EIPId']
            eip_bind = i['Bandwidth']
            hostname = i['Resource']['ResourceName']
            eip_dict[eip] = [eip_id, eip_bind, hostname]
        return eip_dict

    def DescribeShareBandwidth(self):
        api_params = {
            "Action": self.api_DescribeShareBandwidth,
            "PublicKey": self.PublicKey,
            "ProjectId": self.ProjectId,
            "Region": self.region
        }
        r = self.do_request(api_params)
        if not r:
            return -1
        share_eip_list = []
        if not r.has_key("DataSet"):
            return share_eip_list
        if len(r["DataSet"]) == 0:
            return share_eip_list
        if not r["DataSet"][0].has_key("EIPSet"):
            return share_eip_list
        for i in r["DataSet"][0]["EIPSet"]:
            share_eip_list.append(i["EIPAddr"][0]["IP"])
        return share_eip_list

    def GetMetricOverview(self):
        api_params = {
            "Action": self.api_GetMetricOverview,
            "PublicKey": self.PublicKey,
            "ProjectId": self.ProjectId,
            "Region": self.region,
            "Zone": self.zone,
            "ResourceType": "eip",
            "Limit": 200,
            "Offset": 0
        }
        r = self.do_request(api_params)
        if not r:
            return -1
        eip_use_dict = {}
        if not r.has_key('DataSet'):
            return eip_use_dict
        for i in r['DataSet']:
            if not i.has_key('NetworkOutUsage'):
                continue
            eip = i['PublicIps'][0]['IP']
            eip_use_dict[eip] = [i['NetworkOutUsage'], str(round(float(i['NetworkOut']) / 8 / 1024)) + "KB/s"]
        return eip_use_dict

    def DescribeBandwidthPackage(self):
        api_params = {
            "Action": self.api_DescribeBandwidthPackage,
            "PublicKey": self.PublicKey,
            "ProjectId": self.ProjectId,
            "Region": self.region,
            "Limit": 20,
            "Offset": 0
        }
        r = self.do_request(api_params)
        if not r:
            return -1
        eip_package_list = []
        for i in r['DataSets']:
            eip = i['EIPAddr'][0]['IP']
            bandwidth = i['Bandwidth']
            eip_package_list.append([eip, bandwidth])
        return eip_package_list

    def CreateBandwidthPackage(self, bandwidth, eip_id, timeRange):
        api_params = {
            "Action": self.api_CreateBandwidthPackage,
            "PublicKey": self.PublicKey,
            "ProjectId": self.ProjectId,
            "Region": self.region,
            "Bandwidth": bandwidth,
            "EIPId": eip_id,
            "TimeRange": timeRange
        }
        r = self.do_request(api_params)
        if r:
            return 0
        else:
            return -1

    def monitor(self, region, zone, eip_list, bandwidth, timeRange, eip_type="mix"):
        self.region = region
        self.zone = zone
        i = 0
        eip_count = {}
        eip_nomal = {}
        for eip in eip_list:
            eip_count[eip] = 0
            eip_nomal[eip] = 0
        stop_sms = 0
        while 1:
            eip_dict = self.DescribeEIP()
            eip_package_list = self.DescribeBandwidthPackage()
            share_eip_list = self.DescribeShareBandwidth()
            eip_use_dict = self.GetMetricOverview()
            if -1 in (eip_dict, eip_package_list, share_eip_list, eip_use_dict):
                err_list = []
                i += 1
                if not eip_dict:
                    logging.debug("eip_dict: %s" % eip_dict)
                    err_list.append("DescribeEIP")
                elif not eip_package_list:
                    logging.debug("eip_package_list: %s" % eip_package_list)
                    err_list.append("DescribeBandwidthPackage")
                elif not share_eip_list:
                    logging.debug("share_eip_list: %s" % share_eip_list)
                    err_list.append("DescribeShareBandwidth")
                elif not eip_use_dict:
                    logging.debug("eip_use_dict: %s" % eip_use_dict)
                    err_list.append("GetMetricOverview")
                if i == 5:
                    logging.error(self.log_api_fail % err_list)
                    self.send_sms(self.sms_api_fail % err_list)
                time.sleep(self.interval)
                continue
            else:
                if i >= 5:
                    logging.debug(self.log_api_recovery)
                    self.send_sms(self.sms_api_recovery)
                i = 0
            if eip_type == "share" or eip_type == "mix":
                for eip in share_eip_list:
                    if not eip_dict.has_key(eip):
                        continue
                    eip_bind = eip_dict[eip][1]
                    eip_name = eip_dict[eip][2]
                    if not eip_use_dict.has_key(eip):
                        continue
                    eip_percent = eip_use_dict[eip][0]
                    eip_network = eip_use_dict[eip][1]
                    logging.debug(
                        self.log_share_eip_check % (eip_name, eip, eip_percent, eip_network, eip_bind))
            if eip_type == "eip" or eip_type == "mix":
                for eip in eip_list:
                    eip_bind = 0
                    for p in eip_package_list:
                        if p[0] == eip:
                            eip_bind += p[1]
                    if not eip_dict.has_key(eip):
                        continue
                    eip_id = eip_dict[eip][0]
                    eip_bind_1 = eip_dict[eip][1]
                    if eip_bind == 0:
                        eip_bind = eip_bind_1
                    else:
                        eip_bind += eip_bind_1
                    eip_name = eip_dict[eip][2]
                    if not eip_use_dict.has_key(eip):
                        logging.error(self.log_eip_dict_null % eip)
                        continue
                    eip_percent = eip_use_dict[eip][0]
                    eip_network = eip_use_dict[eip][1]
                    if eip_percent > 85:
                        eip_count[eip] += 1
                        if eip in ["120.132.92.17", "123.59.59.123"]:
                            if eip_count[eip] == 3:
                                self.send_sms("%s-%s 带宽超阈值，使用率%s%%，网速%sKb/s，当前带宽%sM，请查看" % (
                                    eip_name, eip, eip_percent, eip_network, eip_bind))
                            continue
                        if eip_bind <= self.alert_bindwidth:
                            logging.error(self.log_keep_check % (
                                eip_name, eip, eip_count[eip], eip_percent, eip_network, eip_bind))
                            code = self.CreateBandwidthPackage(bandwidth, eip_id, timeRange)
                            if code == 0:
                                logging.warn(self.log_buy_package % (
                                    eip_name, eip, eip_bind, bandwidth, timeRange, eip_bind + bandwidth))
                                self.send_sms(self.sms_buy_package % (
                                    eip_name, eip, eip_bind, bandwidth, timeRange, eip_bind + bandwidth))
                            else:
                                logging.error(self.log_buy_package_fail % (
                                    eip_name, eip, eip_bind, bandwidth, timeRange))
                                self.send_sms(self.sms_buy_package_fail % (
                                    eip_name, eip, eip_bind, bandwidth, timeRange))
                            time.sleep(self.interval_buy_wait)
                        else:
                            logging.error(self.log_no_buy_package % (
                                eip_name, eip, eip_count[eip], eip_percent, eip_network, eip_bind,
                                self.alert_bindwidth))
                            if stop_sms == 0:
                                self.send_sms(self.sms_no_buy_package % (
                                    eip_name, eip, eip_percent, eip_network, eip_bind_1, eip_bind))
                                stop_sms = 1
                                eip_nomal[eip] = 0
                    else:
                        eip_nomal[eip] += 1
                        logging.info(self.log_normal % (eip_name, eip, eip_percent, eip_network, eip_bind))
                        eip_count[eip] = 0
                        if stop_sms == 1:
                            eip_nomal[eip] += 1
                            if eip_nomal[eip] == 30:
                                stop_sms = 0
                                eip_nomal[eip] = 0
                    time.sleep(self.interval)

    def run(self):
        bandwidth = 5
        timeRange = 1
        eip_host = {
            "123.59.59.60": "new-nginx-lua-1",
            "123.59.59.115": "new-share-nginx-1",
            "106.75.48.22": "new-siochat-1",
            "180.150.178.13": "new-siochat-2",
            "123.59.59.16": "new-ppt-p2p",
            "123.59.68.181": "Live-new-media-client-log",
            "123.59.139.123": "D-IM-Login-webApi",
            "123.59.65.64": "Live-nginx-lua-1",
            "123.59.56.231": "Live-nginx-lua-2",
            "123.59.87.167": "Live-108-nginx-liveApi-1",
            "120.132.84.140": "Live-108-liveApi-others-1",
            "123.59.56.131": "108-imsocketio-static",
            "120.132.85.50": "C-Live-108-LiveTask",
            "123.59.59.123": "C-Dev",
            "106.75.11.150": "C-Live-150"
        }
        threads = []
        for eip in eip_host.keys():
            t = threading.Thread(target=UcloudBandwidth.monitor,
                                 args=(self, self.region_bj2, self.zone_C, [eip], bandwidth, timeRange))
            threads.append(t)
            t.setDaemon(True)
            t.start()
        for t in threads:
            t.join()

if __name__ == "__main__":
    monitor = UcloudBandwidth()
    monitor.run()
