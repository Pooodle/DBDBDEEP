#infoaddress-infopolicy FK
#사용자 문의(유형,내용)-답변, 회원가입(아이디,나이), 회원탈퇴
#웹프로그래밍


from __future__ import print_function
from datetime import date, datetime, timedelta
import time
import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'silver'


cnx = mysql.connector.connect(user='root', password= 'elqlelqlelq')
cursor = cnx.cursor()

#DB silver 이용
cursor.execute("USE silver")

#오늘날짜
today = datetime.now().date()
now = time.localtime()
userkitchen2Day=now.tm_wday+1 #오늘 요일
#print(userkitchen2Day)

#관리자 비밀번호
adminpassword='elqlelqlelq'

#첫화면
print("-------------------------------------------------------------------------------------------------------")
print("                              경기도 어르신 프로그램을 시작합니다!                    ")
print("-------------------------------------------------------------------------------------------------------")
loop_on_firstpage=False
while not loop_on_firstpage:
	print("")
	print("1.USER 2.ADMIN 3.종료")
	print("")
	whouse=int(input(""))
	if whouse == 1:
		print("")
		print("-------------------------------------------------------------------------------------------------------")
		print("                                 원하시는 서비스를 선택해주세요                    ")
		print("-------------------------------------------------------------------------------------------------------")
		loop_on_user = False
		while not loop_on_user:
			print("")
			print("1.무료급식소 2.병원정보 3.일자리 4.주거요양정보 5.보호기관 6.복지정책 7.첫페이지로")
			print("")
			usermenu=int(input())
			print("")

			#무료급식소 선택 #TRIGGER
			if usermenu == 1:
				print("-------------------------------------------------------------------------------------------------------")
				print("                                        무료급식소 정보  (test:수원)(TRIGGER:요일)                                               ")
				print("-------------------------------------------------------------------------------------------------------")
				print("")
				userkitchenCity=input("선생님이 계신 시/군을 입력해주세요: ")
				print("")

				loop_on_kitchen1 = False
				while not loop_on_kitchen1:

					print("1.월 2.화 3.수 4.목 5.금 6.토 7.일 8.오늘 9.처음으로")
					print("")
					userkitchenDay=int(input("알고싶은 날짜 선택해주세요: "))
					add_userkitchenDay = ("INSERT INTO todayskitchen "
				                                  "(ttody,twantday) "
				                                  "VALUES (%s, %s)")
					data_userkitchenDay =(today,userkitchenDay)
					cursor.execute(add_userkitchenDay,data_userkitchenDay)
					print("")

			        #월요일 선택 
					if userkitchenDay == 1:
						print("-------------------------------------------------------------------------------------------------------")
						print("             월요일  현재 운영 중인  "+ userkitchenCity +"  시(군)의 무료급식소입니다!     " )
						print("-------------------------------------------------------------------------------------------------------")
						print("|    센터명    |    운영시간    |  이용조건  |       장소       |               주소                |   전화번호  |")
						print("")
						cursor.execute("SELECT kName, hour, target, place, address2, phone FROM kitchensoup where isopen='Y' and city LIKE %s ORDER BY kName", ("%" + userkitchenCity + "%",)) #%s LIMIT 1 결과 하나만
						for (kName, hour, target, place, address2, phone) in cursor:
						  print("|{} | {} | {} | {} | {} | {}|".format(
						    kName, hour, target, place, address2, phone))

				    #화요일 선택
					elif userkitchenDay == 2:
						print("-------------------------------------------------------------------------------------------------------")
						print("             화요일  현재 운영 중인  " + userkitchenCity +"  시(군)의 무료급식소입니다!     " )
						print("-------------------------------------------------------------------------------------------------------")
						print("|    센터명    |    운영시간    |  이용조건  |       장소       |               주소                |   전화번호  |")
						print("")
						cursor.execute("SELECT kName, hour, target, place, address2, phone FROM kitchensoup where isopen='Y' and city LIKE %s ORDER BY kName", ("%" + userkitchenCity + "%",)) #%s LIMIT 1 결과 하나만
						for (kName, hour, target, place, address2, phone) in cursor:
						  print("|{} | {} | {} | {} | {} | {}|".format(
						    kName, hour, target, place, address2, phone))

					#수요일 선택
					elif userkitchenDay == 3:
						print("-------------------------------------------------------------------------------------------------------")
						print("             수요일  현재 운영 중인  " + userkitchenCity +"  시(군)의 무료급식소입니다!     " )
						print("-------------------------------------------------------------------------------------------------------")
						print("|    센터명    |    운영시간    |  이용조건  |       장소       |               주소                |   전화번호  |")
						print("")
						cursor.execute("SELECT kName, hour, target, place, address2, phone FROM kitchensoup where isopen='Y' and city LIKE %s ORDER BY kName", ("%" + userkitchenCity + "%",)) #%s LIMIT 1 결과 하나만
						for (kName, hour, target, place, address2, phone) in cursor:
						  print("|{} | {} | {} | {} | {} | {}|".format(
						    kName, hour, target, place, address2, phone))

					#목요일 선택
					elif userkitchenDay == 4:
						print("-------------------------------------------------------------------------------------------------------")
						print("             목요일  현재 운영 중인  " + userkitchenCity +"  시(군)의 무료급식소입니다!     " )
						print("-------------------------------------------------------------------------------------------------------")
						print("|    센터명    |    운영시간    |  이용조건  |       장소       |               주소                |   전화번호  |")
						print("")
						cursor.execute("SELECT kName, hour, target, place, address2, phone FROM kitchensoup where isopen='Y' and city LIKE %s ORDER BY kName", ("%" + userkitchenCity + "%",)) #%s LIMIT 1 결과 하나만
						for (kName, hour, target, place, address2, phone) in cursor:
						  print("|{} | {} | {} | {} | {} | {}|".format(
						    kName, hour, target, place, address2, phone))

					#금요일 선택
					elif userkitchenDay == 5:
						print("-------------------------------------------------------------------------------------------------------")
						print("             금요일  현재 운영 중인  " + userkitchenCity +"  시(군)의 무료급식소입니다!     " )
						print("-------------------------------------------------------------------------------------------------------")
						print("|    센터명    |    운영시간    |  이용조건  |       장소       |               주소                |   전화번호  |")
						print("")
						cursor.execute("SELECT kName, hour, target, place, address2, phone FROM kitchensoup where isopen='Y' and city LIKE %s ORDER BY kName", ("%" + userkitchenCity + "%",)) #%s LIMIT 1 결과 하나만
						for (kName, hour, target, place, address2, phone) in cursor:
						  print("|{} | {} | {} | {} | {} | {}|".format(
						    kName, hour, target, place, address2, phone))

					#토요일 선택
					elif userkitchenDay == 6:
						print("-------------------------------------------------------------------------------------------------------")
						print("             토요일  현재 운영 중인  " + userkitchenCity +"  시(군)의 무료급식소입니다!     " )
						print("-------------------------------------------------------------------------------------------------------")
						print("|    센터명    |    운영시간    |  이용조건  |       장소       |               주소                |   전화번호  |")
						print("")
						cursor.execute("SELECT kName, hour, target, place, address2, phone FROM kitchensoup where isopen='Y' and city LIKE %s ORDER BY kName", ("%" + userkitchenCity + "%",)) #%s LIMIT 1 결과 하나만
						for (kName, hour, target, place, address2, phone) in cursor:
						  print("|{} | {} | {} | {} | {} | {}|".format(
						    kName, hour, target, place, address2, phone))

					#일요일 선택
					elif userkitchenDay == 7:
						print("-------------------------------------------------------------------------------------------------------")
						print("             일요일  현재 운영 중인  " + userkitchenCity +"  시(군)의 무료급식소입니다!     " )
						print("-------------------------------------------------------------------------------------------------------")
						print("|    센터명    |    운영시간    |  이용조건  |       장소       |               주소                |   전화번호  |")
						print("")
						cursor.execute("SELECT kName, hour, target, place, address2, phone FROM kitchensoup where isopen='Y' and city LIKE %s ORDER BY kName", ("%" + userkitchenCity + "%",)) #%s LIMIT 1 결과 하나만
						for (kName, hour, target, place, address2, phone) in cursor:
						  print("|{} | {} | {} | {} | {} | {}|".format(
						    kName, hour, target, place, address2, phone))

					#오늘 선택
					elif userkitchenDay == 8:
						add_userkitchen2Day = ("INSERT INTO todayskitchen "
							                         "(ttody,twantday) "
					                                 "VALUES (%s, %s)")
						data_userkitchen2Day =(today,userkitchen2Day)
						cursor.execute(add_userkitchen2Day,data_userkitchen2Day)
						print("-------------------------------------------------------------------------------------------------------")
						print("             오늘  현재 운영 중인  " + userkitchenCity +"  시(군)의 무료급식소입니다!     " )
						print("-------------------------------------------------------------------------------------------------------")
						print("")
						print("|    센터명    |    운영시간    |  이용조건  |       장소       |               주소                |   전화번호  |")
						cursor.execute("SELECT kName, hour, target, place, address2, phone FROM kitchensoup where isopen='Y' and city LIKE %s ORDER BY kName", ("%" + userkitchenCity + "%",)) #%s LIMIT 1 결과 하나만
						for (kName, hour, target, place, address2, phone) in cursor:
						  print("|{} | {} | {} | {} | {} | {}|".format(
						    kName, hour, target, place, address2, phone))
					
					elif userkitchenDay == 9:
						loop_on_kitchen1 = True

					else :
						print("")
						print("*********잘못선택하셨습니다.다시 선택해주세요***********")
						print("")
						print("")

			#병원선택 VIEW
			elif usermenu == 2:
				print("-------------------------------------------------------------------------------------------------------")
				print("                                    병원 정보    (1.test:용인 ,3.test:의정부)(VIEW:3-2-1)                ")
				print("-------------------------------------------------------------------------------------------------------")
				
				loop_on_hospital1 = False
				while not loop_on_hospital1:
					print("")
					print("1.지역별 병원 정보 2.어르신 전문병원 3.치매센터 4.처음으로")
					print("")
					userhospitalWhat=int(input("원하시는 서비스를 선택해주세요: "))
					print("")
					if userhospitalWhat == 1:
						print("")
						userhospitalCity=input("선생님이 계신 시/군을 입력해주세요: ")
						print("")
						print("-------------------------------------------------------------------------------------------------------")
						print("                 " + userhospitalCity +"  시(군)의 어르신 전문병원과 치매센터입니다!     " )
						print("-------------------------------------------------------------------------------------------------------")
						print("")
						print("|    유형    |        시설명         |    전화번호    |                     주소                   |")
						cursor.execute("SELECT htype, hName, phone, address2 FROM hospital where city LIKE %s ORDER BY htype, hName", ("%" + userhospitalCity + "%",)) #%s LIMIT 1 결과 하나만
						for (htype, hName, phone, address2) in cursor:
						  print("|{} | {} | {} | {}|".format(
						    htype, hName, phone, address2))
						print("")

					elif userhospitalWhat == 2:
						print("-------------------------------------------------------------------------------------------------------")
						print("                                       어르신 전문병원 정보                                             " )
						print("-------------------------------------------------------------------------------------------------------")
						print("")
						print("| 지역 |       시설명        | 병상수 |                진료과목                |       홈페이지      |             주소                   |")
						cursor.execute("SELECT city, hName, bedNum, intro, homepage, address2 FROM hospital where htype = '노인전문병원' ORDER BY city, hName") #%s LIMIT 1 결과 하나만
						for (city,hName, bedNum, intro, homepage, address2) in cursor:
						  print("|{} | {} | {} | {} | {}| {} | ".format(
						    city,hName, bedNum, intro, homepage, address2))
						print("")

					elif userhospitalWhat == 3:
					
						loop_on_hospital2 = False
						while not loop_on_hospital2:
							print("")
							print("1.전체 2.지역별 3.다른 정보")
							print("")
							userdemntiaScaleNum=int(input())
							if userdemntiaScaleNum == 1:	
								print("")
								print("-------------------------------------------------------------------------------------------------------")
								print("                                            전체 치매센터 정보                  " )
								print("-------------------------------------------------------------------------------------------------------")
								print("")
								print("| 지역 |        센터명         |      전화번호    |                    주소                     |")
								cursor.execute("SELECT city, hName, phone , address2 FROM hospital where htype like '%치매%' ORDER BY city, hName") #%s LIMIT 1 결과 하나만
								for (city, hName, phone , address2) in cursor:
								  print("|{} | {} | {} | {}|".format(
								    city, hName, phone , address2))
								print("")	

							elif userdemntiaScaleNum == 2:
								print("")
								userdemntiaScaleCity=input("선생님이 계신 시/군을 입력해주세요: ")
								print("")	
								loop_on_hospital3 = False
								while not loop_on_hospital3:
									print("")
									print("1.치매검사가능센터 2.치매센터별 의료진 정보 3.다른 치매센터 정보")
									print("")
									userdemntiaScaledetail=int(input())
									print("")
									if userdemntiaScaledetail == 1:	
										print("")
										print("-------------------------------------------------------------------------------------------------------")
										print("                  " + userdemntiaScaleCity +"  시(군)의 치매 검사가 가능한 센터                  " )
										print("-------------------------------------------------------------------------------------------------------")
										print("")
										print("|       센터명     |   전화번호   |                 주소                 |                      설명                     |")
										cursor.execute("SELECT hName, phone , address1, intro FROM dementiaScale where city LIKE %s ORDER BY hname", ("%" + userdemntiaScaleCity + "%",)) #%s LIMIT 1 결과 하나만
										for (hName, phone , address1, intro) in cursor:
										  print("|{} | {} | {}| {}|".format(
										    hName, phone , address1, intro))
										print("")

									elif userdemntiaScaledetail == 2:	
										print("")
										print("-------------------------------------------------------------------------------------------------------")
										print("                  " + userdemntiaScaleCity +"  시(군) 치매 센터의 의료진 정보                  " )
										print("-------------------------------------------------------------------------------------------------------")
										print("")
										print("|       센터명     |   전화번호   |                 주소                | 의사 | 간호사 | 사회복지사 | 전문치료사 |")
										cursor.execute("SELECT hName, phone , address1, doctorNum, nurseNum, socialwokerNum, therapistNum  FROM hospital where city LIKE %s ORDER BY hname", ("%" + userdemntiaScaleCity + "%",)) #%s LIMIT 1 결과 하나만
										for (hName, phone , address1, doctorNum, nurseNum, socialwokerNum, therapistNum) in cursor:
										  print("|{} | {} | {} |  {}  |  {}  |  {}  |  {}  |".format(
										    hName, phone , address1, doctorNum, nurseNum, socialwokerNum, therapistNum))
										print("")	
									
									elif userdemntiaScaledetail == 3:
										loop_on_hospital3 = True
									else :
										print("")
										print("*********잘못선택하셨습니다.다시 선택해주세요***********")
										print("")

							elif userdemntiaScaleNum == 3:
								loop_on_hospital2 = True
										
							else :
								print("")
								print("*********잘못선택하셨습니다.다시 선택해주세요***********")
								print("")

					elif userhospitalWhat == 4:
						loop_on_hospital1 = True		
					else :
						print("")
						print("*********잘못선택하셨습니다.다시 선택해주세요***********")
						print("")
						print("")
			
			elif usermenu == 3:
				print("-------------------------------------------------------------------------------------------------------")
				print("                                       일자리 정보  (test:성남, 시흥)(1.OLAP,2.NATURAL JOIN)                                               ")
				print("-------------------------------------------------------------------------------------------------------")
				loop_on_employ1 = False
				while not loop_on_employ1:
					print("")
					print("1.유형별 전체 일자리 개수 2.지역별 일자리 보기 3.처음으로")
					print("")
					print("원하시는 서비스를 선택해주세요.")
					employservice0=int(input())
					if employservice0 == 1:
						print("-------------------------------------------------------------------------------------------------------")
						print("                                      유형별 전체 일자리 개수                                            " )
						print("-------------------------------------------------------------------------------------------------------")
						print("")
						print("|  지역  |   유형   | 일자리 현황 |")
						cursor.execute("SELECT ecity, etype, count(etype) as number from employ join employcenter on employ.eAdmincode = employcenter.eAdmincode group by ecity, etype order by ecity")
						for (ecity, etype, count) in cursor:
						  print("| {} |   {}   |    {}    |".format(
						    ecity, etype, count))
						print("")

					elif employservice0 == 2:	
						loop_on_employ3 = False
						while not loop_on_employ3:
							print("")
							print("[처음으로 가시려면 5를 눌러주세요]")
							useremployCity=input("선생님이 계신 시/군을 입력해주세요: ")
							if useremployCity == '5':
								loop_on_employ3 = True
							else:
								print("")
								print("-------------------------------------------------------------------------------------------------------")
								print("                           " + useremployCity +"  시(군)의 일자리 현황                                  " )
								print("-------------------------------------------------------------------------------------------------------")
								print("")
								print("|   일자리명  | 유형 |     전화번호    |                        주소                       |   관리센터  | 센터 전화번호 |")
								cursor.execute("SELECT eName, etype, ephone , eaddress2, ecName, ecphone FROM employdemension where ecity LIKE %s ORDER BY ename", ("%" + useremployCity + "%",)) #%s LIMIT 1 결과 하나만
								for (eName, etype, ephone , eaddress2, ecName, ecphone) in cursor:
								  print("|{} | {} | {} | {} | {} | {}|".format(
								    eName, etype, ephone , eaddress2, ecName, ecphone))
								print("")
								loop_on_employ2 = False
								while not loop_on_employ2:
									print("")
									print("1."+useremployCity+"시(군) 일자리센터 정보 보기 2.다른 지역 찾기")
									useremployDetail=int(input())
									print("")
									if useremployDetail == 1:
										print("-------------------------------------------------------------------------------------------------------")
										print("                           " + useremployCity +"  시(군)의 일자리 센터 정보                                  " )
										print("-------------------------------------------------------------------------------------------------------")
										print("")
										print("|     센터명     |   전화번호   |                주소                |      운영재단     | 근로자수 | 이용자수 | 지자체 직영(D) 위탁(C)")
										cursor.execute("SELECT ecName, ecphone, ecaddress1, edAdmin, wokerNum, userNum, foundation FROM employcenter natural join employcenter_Detail where eccity LIKE %s ORDER BY ecname", ("%" + useremployCity + "%",)) #%s LIMIT 1 결과 하나만
										for (ecName, ecphone, ecaddress1, edAdmin, wokerNum, userNum, foundation) in cursor:
										  print("|{} | {} | {} | {} | {} | {} | {}|".format(
										    ecName, ecphone, ecaddress1, edAdmin, wokerNum, userNum, foundation))
										print("")

									elif useremployDetail == 2:
										loop_on_employ2 = True
									else :
										print("*********잘못선택하셨습니다.다시 선택해주세요***********")

					elif employservice0 == 3:
						loop_on_employ1 = True
					else :
						print("*********잘못선택하셨습니다.다시 선택해주세요***********")	

			elif usermenu == 4:
				print("-------------------------------------------------------------------------------------------------------")
				print("                            주거요양 정보    (test: 안산 )                                 ")
				print("-------------------------------------------------------------------------------------------------------")

				print("")
				userresidenceCity=input("선생님이 계신 시/군을 입력해주세요: ")
				print("")

				loop_on_residence = False
				while not loop_on_residence:
					print("")
					print("1.수용가능 요양시설 2.기초수급자 수용가능 시설 3.처음으로")
					print("")
					userresidenceWhat=int(input("원하시는 서비스를 선택해주세요: "))
					print("")
					if userresidenceWhat == 1:
						print("-------------------------------------------------------------------------------------------------------")
						print("                 " + userresidenceCity +"  시(군)의 수용가능한 요양시설입니다!                           " )
						print("-------------------------------------------------------------------------------------------------------")
						print("")
						print("|  지역  |     시설명      |    전화번호    |                     주소                   | 잔여수용가능인원 |")
						cursor.execute("SELECT city, rName, rphone, address2, capacity-capacity_now as acceptable FROM residence_home where city LIKE %s AND capacity > capacity_now ORDER BY city", ("%" + userresidenceCity + "%",)) #%s LIMIT 1 결과 하나만
						for (city, rName, rphone, address2, acceptable) in cursor:
							print("| {} |  {}  | {} | {} | {} |".format(
								city, rName, rphone, address2, acceptable))
						print("")

					elif userresidenceWhat == 2:
						print("-------------------------------------------------------------------------------------------------------")
						print("              " + userresidenceCity +"  시(군)의 기초수급자 수용가능 시설입니다!                          " )
						print("-------------------------------------------------------------------------------------------------------")
						print("")
						print("|  지역  |     시설명      |    전화번호    |                     주소                   |")
						cursor.execute("SELECT city, rName, rphone, address2 FROM residence WHERE city LIKE %s AND publicassistance='Y' order by city", ("%" + userresidenceCity + "%",)) #%s LIMIT 1 결과 하나만
						for (city, rName, rphone, address2) in cursor:
							print("| {} |  {}  | {} | {} |".format(
								city, rName, rphone, address2))
						print("")
					
					elif userresidenceWhat == 3:
						loop_on_residence = True
					
					else :
						print("")
						print("*********잘못선택하셨습니다.다시 선택해주세요***********")
						print("")
						print("")

			elif usermenu == 5:
				print("-------------------------------------------------------------------------------------------------------")
				print("                                    보호기관 정보    (2.test: 부천)                                      ")
				print("-------------------------------------------------------------------------------------------------------")
				
				loop_on_protection = False
				while not loop_on_protection:
					print("")
					print("1.전체 보호기관 2.지역별 보호기관 3.처음으로")
					print("")
					userprotectionWhat=int(input("원하시는 서비스를 선택해주세요: "))
					print("")
					if userprotectionWhat == 1:
						print("-------------------------------------------------------------------------------------------------------")
						print("                                   전체 지역의 보호기관 입니다!                                          " )
						print("-------------------------------------------------------------------------------------------------------")
						print("")
						print("|  지역  |     보호기관명      |    전화번호    |                     주소                   |")
						cursor.execute("SELECT * FROM protection_all")
						for (cpcity, cpame, cpphone, cpaddress) in cursor:
							print("| {} |  {}  | {} | {} |".format(
								cpcity, cpame, cpphone, cpaddress))
						print("")

					elif userprotectionWhat == 2:
						print("")
						userprotectionCity=input("선생님이 계신 시/군을 입력해주세요: ")
						print("")
						print("-------------------------------------------------------------------------------------------------------")
						print("                   " + userprotectionCity +"  시(군)의 노인 보호기관입니다!                              " )
						print("-------------------------------------------------------------------------------------------------------")
						print("")
						print("|  지역  |     보호기관명      |    전화번호    |                     주소                   |")
						cursor.execute("SELECT * FROM protection_all WHERE cpcity LIKE %s", ("%" + userprotectionCity + "%",))
						for (cpcity, cpame, cpphone, cpaddress) in cursor:
							print("| {} |  {}  | {} | {} |".format(
								cpcity, cpame, cpphone, cpaddress))
						print("")

					elif userprotectionWhat == 3:
						loop_on_protection = True

					else :
						print("")
						print("*********잘못선택하셨습니다.다시 선택해주세요***********")
						print("")
						print("")
	

			elif usermenu == 6:
				print("-------------------------------------------------------------------------------------------------------")
				print("                          노인복지정책 정보    (1.test: 일자리 2.test: 급여)                             ")
				print("-------------------------------------------------------------------------------------------------------")
				
				loop_on_policy = False
				while not loop_on_policy:
					print("")
					print("1.유형별 복지정책 2.정책 내용 3.처음으로")
					print("")
					userpolicyWhat=int(input("원하시는 서비스를 선택해주세요: "))
					print("")
					if userpolicyWhat == 1:
						print("")
						print("유형: 병원, 보호기관, 일자리, 주거요양")
						userpolicyType=input("궁금하신 노인복지정책 유형을 입력해주세요: ")
						print("")
						print("-------------------------------------------------------------------------------------------------------")
						print("                         " + userpolicyType +"  유형의 노인복지정책입니다!                                " )
						print("-------------------------------------------------------------------------------------------------------")
						print("")
						print("|    관련시설명    |     노인복지정책명      |                     설명                   |    전화번호    |")
						cursor.execute("SELECT iAName, iName, intro, iAphone FROM policy where itype LIKE %s", ("%" + userpolicyType + "%",))
						for (iAName, iName, intro, iAphone) in cursor:
							print("| {} |  {}  | {} | {} |".format(
								iAName, iName, intro, iAphone))
						print("")
	
					elif userpolicyWhat == 2:
						print("")
						print("급여, 일자리, 주택, 교육, 치료, 독거노인 등")
						userpolicyContent=input("궁금하신 노인복지정책 내용을 입력해주세요: ")
						print("")
						print("-------------------------------------------------------------------------------------------------------")
						print("                     " + userpolicyContent +" 와 관련된 노인복지정책입니다!                              " )
						print("-------------------------------------------------------------------------------------------------------")
						print("")
						print("|    관련시설명    |     노인복지정책명      |                     설명                   |    전화번호    |")
						cursor.execute("SELECT iAName, iName, intro, iAphone FROM policy where iName LIKE %s", ("%" + userpolicyContent + "%",))
						for (iAName, iName, intro, iAphone) in cursor:
							print("| {} |  {}  | {} | {} |".format(
								iAName, iName, intro, iAphone))
						print("")
	
					elif userpolicyWhat == 3:
						loop_on_policy = True

					else :
						print("")
						print("*********잘못선택하셨습니다.다시 선택해주세요***********")
						print("")
						print("")


			elif usermenu == 7:
				loop_on_user = True

			else :
				print("")
				print("***********준비 중 입니다************")
				print("")

						

	elif whouse == 2:
		print("")
		print("-------------------------------------------------------------------------------------------------------")
		print("                                   ADMIN LOGIN PAGE (PW:디비딥)(REFERENTIAL INTEGRITY)                                              ")
		print("-------------------------------------------------------------------------------------------------------")
		loop_on_Admin1 = False
		while not loop_on_Admin1:
			print("")
			print("[5를 입력하면 첫페이지로]")
			print("")
			print("")
			adminPWtry=input("PASSWORD: ")
			print("")
			if adminPWtry == '디비딥':
				print("")	
				print("-------------------------------------------------------------------------------------------------------")
				print("                                         LOGIN SUCCESS! (3.일자리)                                            ")
				print("-------------------------------------------------------------------------------------------------------")
				loop_on_Admin2 = False
				while not loop_on_Admin2:
					print("")
					print("관리할 서비스를 선택하세요.")
					print("")
					print("1.무료급식소 2.병원정보 3.일자리 4.주거요양정보 5.보호기관 6.복지정책 7.첫페이지로")
					print("")
					adminselect=int(input())
					
					if adminselect == 3:
						print("")	
						print("-------------------------------------------------------------------------------------------------------")
						print("                                     일자리 서비스 관리 페이지입니다. (test:수원, 성남)                              ")
						print("-------------------------------------------------------------------------------------------------------")
						loop_on_Admin3 = False
						while not loop_on_Admin3:
							print("")
							print("1. 기존 일자리센터 삭제  2. 새로운 일자리 입력 3.처음으로")
							print("")
							adminemploy=int(input())
							print("")
							if adminemploy == 1:
								adminempcenter_city=input("관리할 지역을 입력해주세요: ")
								print("| 지역 | 코드 |     센터명     |   전화번호   | 해당 센터 일자리 ")
								cursor.execute("SELECT eccity, eAdmincode, ecName, ecphone, eName FROM employcenter natural join employ where eccity LIKE %s ORDER BY eAdmincode", ("%" + adminempcenter_city + "%",)) #%s LIMIT 1 결과 하나만
								for (eccity, eAdmincode, ecName, ecphone, eName) in cursor:
								  print("|{} | {} | {} | {} | {} |".format(
								    eccity, eAdmincode, ecName, ecphone, eName))
								print("")
								print("")
								print("삭제 전 fk로 연결 된 employcenter_Detail 테이블")
								cursor.execute("SELECT eAdmincode,edAdmin, edName, wokerNum, userNum, foundation FROM employcenter_Detail natural join employcenter where eccity LIKE %s ORDER BY eAdmincode", ("%" + adminempcenter_city + "%",))
								for (eAdmincode,edAdmin, edName, wokerNum, userNum, foundation) in cursor:
								  print("|{} | {} | {} | {} | {} | {} |".format(
								    eAdmincode,edAdmin, edName, wokerNum, userNum, foundation))

								print("")
								print("")
								print("삭제 전 fk로 연결 된 employ 테이블")
								cursor.execute("SELECT eAdmincode, ecode, eID, ecity, eName, etype, ephone, elatitude, elongitude FROM employ where ecity LIKE %s ORDER BY eAdmincode", ("%" + adminempcenter_city + "%",))
								for (eAdmincode, ecode, eID, ecity, eName, etype, ephone, elatitude, elongitude) in cursor:
								  print("|{} | {} | {} | {} | {} | {} | {} | {} | {} |".format(
								    eAdmincode, ecode, eID, ecity, eName, etype, ephone, elatitude, elongitude))
								
								print("")
								adminempcenter_del=input("삭제할 센터의 코드를 입력해주세요: ")
								
								try:
									employ_Delete_query = """Delete from employcenter where eAdmincode = %s"""
									cursor.execute(employ_Delete_query,(adminempcenter_del,))
									print("\n삭제 성공")

								except mysql.connector.Error as error:
									print("삭제 실패: {}".format(error))
								
								print("삭제 후 employcenter 테이블")
								cursor.execute("SELECT eccity, eAdmincode, ecName, ecphone, eName FROM employcenter natural join employ where eccity LIKE %s ORDER BY eAdmincode", ("%" + adminempcenter_city + "%",)) #%s LIMIT 1 결과 하나만
								for (eccity, eAdmincode, ecName, ecphone, eName) in cursor:
								  print("|{} | {} | {} | {} | {} |".format(
								    eccity, eAdmincode, ecName, ecphone, eName))
								print("")
								print("삭제 후 fk로 연결된 employcenter_Detail 테이블")
								cursor.execute("SELECT eAdmincode,edAdmin, edName, wokerNum, userNum, foundation FROM employcenter_Detail natural join employcenter where eccity LIKE %s ORDER BY eAdmincode", ("%" + adminempcenter_city + "%",))
								for (eAdmincode,edAdmin, edName, wokerNum, userNum, foundation) in cursor:
								  print("|{} | {} | {} | {} | {} | {} |".format(
								    eAdmincode,edAdmin, edName, wokerNum, userNum, foundation))
								print("")
								print("삭제 후 fk로 연결된 employ 테이블")
								cursor.execute("SELECT eAdmincode, ecode, eID, ecity, eName, etype, ephone, elatitude, elongitude FROM employ where ecity LIKE %s ORDER BY eAdmincode", ("%" + adminempcenter_city + "%",))
								for (eAdmincode, ecode, eID, ecity, eName, etype, ephone, elatitude, elongitude) in cursor:
								  print("|{} | {} | {} | {} | {} | {} | {} | {} | {} |".format(
								    eAdmincode, ecode, eID, ecity, eName, etype, ephone, elatitude, elongitude))
								print("")

							elif adminemploy == 2:
								print("")
								print("관리자 코드 목록")
								cursor.execute("SELECT eccity, ecName, eAdmincode FROM employcenter ORDER BY eccity,ecName") 
								for (eccity, ecName, eAdmincode) in cursor:
								  print("|{} | {} | {} |".format(
								    eccity, ecName, eAdmincode))
						
								print("")
								print("삽입할 데이터를 입력하세요")
								empoyinsert1=input("지역: ")
								empoyinsert2=input("일자리명: ")
								empoyinsert3=input("유형: ")
								empoyinsert4=input("관리자 코드: ")
								empoyinsert5=input("전화번호: ")
								empoyinsert6=input("주소: ")

								try:
									add_user_employcenter = ("INSERT INTO employ"
									               "(ecode, ecity, eName, etype, eAdmincode, ephone, eaddress2) "
									               "VALUES (%s, %s, %s, %s, %s, %s, %s)")
									data_user_employcenter=('일자리',empoyinsert1,empoyinsert2,empoyinsert3,empoyinsert4,empoyinsert5,empoyinsert6)
									cursor.execute(add_user_employcenter,data_user_employcenter)

									print("")
									print("추가된 일자리")
									cursor.execute("SELECT eName, etype, ephone , eaddress2, ecName, ecphone FROM employdemension where eName LIKE %s", ("%" + empoyinsert2 + "%",)) #%s LIMIT 1 결과 하나만
									for (eName, etype, ephone , eaddress2, ecName, ecphone) in cursor:
									  print("|{} | {} | {} | {} | {} | {}|".format(
									    eName, etype, ephone , eaddress2, ecName, ecphone))

								except mysql.connector.Error as error:
									print("-------------------------------------------------------------------------------------------------------")
									print("employcenter(부모테이블)에 존재하지 않는 key(eAdmincode)갖는 데이터(관리자 코드) 삽입 오류")
									print("-------------------------------------------------------------------------------------------------------")
									print("*************참조무결성 위배: 일자리 센터에 있는 코드를 입력해주세요************8: {}".format(error))


							elif adminemploy == 3:
								loop_on_Admin3 = True

							else :
								print("")
								print("*********잘못선택하셨습니다.다시 선택해주세요***********")
								print("")

					elif adminselect == 7:
						loop_on_Admin2 = True
						loop_on_Admin1 = True

					else:
						print("")
						print("***********준비 중 입니다************")
						print("")
						

			elif adminPWtry == '5':
				loop_on_Admin1 = True
			else :
				print("")	
				print("***********************LOGIN FAIL;(**********************************")	

	elif whouse == 3:
		loop_on_firstpage=True

	else:
		print("")
		print("*********잘못선택하셨습니다.다시 선택해주세요***********")
		print("")


# Make sure data is committed to the database
cnx.commit()

cursor.close()  
cnx.close()