import requests
import json
import time
import os

def url_vi():
    while(1):
        time.sleep(3)
        try:
            f = open("./intput.txt", "r")
        except:
            print("1why??")
            continue
        scan_url = ""
        line = f.readline()
        if(scan_url == line.replace('"', '')):
            continue
        scan_url = line.replace('"', '')
        f.close()
        os.remove('intput.txt')

        # 바이러스토탈 API key
        my_apikey = 'e8b735cd572c86e1b73f898221b6a7db7fdd6f5250fc53ca788aad46137da664' 

        # 바이러스 토탈 URL 스캔
        url = 'https://www.virustotal.com/vtapi/v2/url/scan'

        # 바이러스토탈 URL 스캔 시작
        params = {'apikey': my_apikey, 'url': scan_url}
        response_scan = requests.post(url, data=params)
        
        
        
        try:
            result_scan = response_scan.json()
            scan_id = result_scan['scan_id']  # 결과를 출력을 위해 scan_id 값 저장
        except:
            print("2")
            continue

        # URL 스캔 시작 안내
        print('Virustotal File Scan Start : ', scan_url, '\n')

        # 스캔 후 1분 대기
        time.sleep(5)
        #
        # 바이러스토탈 URL 스캔 결과 주소
        url_report = 'https://www.virustotal.com/vtapi/v2/url/report'

        # 결과 파일 찾기 위해 scan_id 입력
        url_report_params = {'apikey': my_apikey, 'resource': scan_id}

        # 바이러스토탈 URL 스캔 결과 리포트 조회
        response_report = requests.get(url_report, params=url_report_params)

        # 점검 결과 데이터 추출
        try:
            report = response_report.json()  # 결과 값을 report에 json형태로 저장
        except:
            print("3")
            continue

        report_verbose_msg = report.get('verbose_msg')
        report_scans = report.get('scans')  # scans 값 저장
        report_scans_vendors = list(report['scans'].keys())  # Vendor 저장
        report_scans_vendors_cnt = len(report_scans_vendors)  # 길이 저장
        report_scan_data = report.get('scan_data')

        print(report_verbose_msg, '\n')
        #time.sleep(1)

        # 파일 스캔 결과 리포트 데이터 보기
        print('Scan Data (UTC) :', report_scan_data)
        print('Scan URL Vendor CNT: ', report_scans_vendors_cnt, '\n')

        # 바이러스 스캔 엔진사 별 데이터 정리

        numbers = 1
        check_virus = 0
        for vendor in report_scans_vendors:
            outputs = report_scans[vendor]
            outputs_result = report_scans[vendor].get('result')
            outputs_detected = report_scans[vendor].get('detected')

        # outputs_detected = True, False
        # outputs_result = clean site, unrated site, malware site, malicious site, Phishing site
            #print(outputs_result)
            if outputs_result != 'clean site':
                if outputs_result != 'unrated site':
                    print(f'[No].{numbers}',
                            ",[Vendor Name]:", vendor,
                            ',[Vendor Result]:', outputs_result,
                            ',[Vendor Detected]:', outputs_detected)
                    check_virus += 1
            numbers += 1

        if(check_virus != 0):
            print("악성 요소가 있는 페이지입니다.")
            print(check_virus)
        else:
            print("안전한 페이지입니다.")
        #time.sleep(15)
        return scan_url

def main():
    url_vi()
    
if __name__ == '__main__':
    main()