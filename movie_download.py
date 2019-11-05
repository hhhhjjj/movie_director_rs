# coding=utf-8
from efficient_apriori import apriori
from lxml import etree
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

directors = ['任景丰', '张石川', '邵醉翁', '但杜宇', '郑正秋', '杨小仲', '程步高', '朱石麟', '万古蟾', '孙瑜', '史东山', '卜万苍', '沈西苓', '应云卫', '马徐维邦', '沈浮', '蔡楚生', '费穆', '吴永刚', '袁牧之', '汤晓丹', '陈鲤庭', '张骏祥', '郑君里', '桑弧', '崔嵬', '王苹', '水华', '成荫', '凌子风', '李俊', '郭维', '王炎', '谢晋', '谢铁骊', '沈耀庭', '丁荫楠', '吴贻弓', '黄蜀芹', '吴天明', '颜学恕', '张暖忻', '陆小雅', '于本正', '翟俊杰', '黄健中', '谢飞', '郑洞天', '滕文骥', '张艺谋', '张建亚', '田壮壮', '陈凯歌', '张军钊', '吴子牛', '夏钢', '周晓文', '黄建新', '冯小宁', '李少红', '何平', '顾长卫', '张元', '王超', '路学长', '娄烨', '王全安', '王小帅', '张扬', '曹保平', '管虎', '贾樟柯', '陆川', '米家山', '郑晓龙', '杨亚洲', '霍建起', '冯小刚', '李杨', '张律', '张一白', '姜文', '朱文', '刁亦男', '丁晟', '马俪文', '徐峥', '乌尔善', '徐浩峰', '李玉', '徐静蕾', '赵薇', '宁浩', '陈思诚', '邓超', '董成鹏', '韩寒', '郭敬明', '张嘉佳', '易小星', '毕赣', '黎民伟', '罗维', '张彻', '李翰祥', '王天林', '胡金铨', '刘家良', '李小龙', '许冠文', '袁和平', '吴宇森', '许鞍华', '方育平', '杨凡', '谭家明', '徐克', '张婉婷', '严浩', '刘镇伟', '程小东', '成龙', '林岭东', '杜琪峰', '王晶', '关锦鹏', '尔冬升', '王家卫', '高志森', '陈果', '刘伟强', '陈嘉上', '唐季礼', '陈木胜', '周星驰', '陈可辛', '叶伟信', '许诚毅', '彭发', '林超贤', '郑保瑞', '彭浩翔', '李行', '白景瑞', '陈坤厚', '王童', '侯孝贤', '杨德昌', '吴念真', '张艾嘉', '李安', '赖声川', '蔡明亮', '陈国富', '林正盛', '易智言', '张作骥', '陈玉勋', '钮承泽', '戴立忍', '魏德圣', '周杰伦', '陈正道', '内田吐梦', '沟口健二', '小津安二郎', '成濑巳喜男', '黑泽明', '新藤兼人', '木下惠介', '市川昆', '小林正树', '冈本喜八', '铃木清顺', '今村昌平', '敕使河原宏', '深作欣二', '筱田正浩', '山田洋次', '大岛渚', '寺山修司', '若松孝二', '小栗康平', '北野武', '原田真人', '崔洋一', '森田芳光', '中原俊', '黑泽清', '中岛哲也', '三池崇史', '园子温', '是枝裕和', '桥口亮辅', '岩井俊二', '萨布', '矢口史靖', '河濑直美', '西川美和', '山下敦弘', '深田晃司', '高畑勋', '宫崎骏', '近藤喜文', '押井守', '大友克洋', '原惠一', '庵野秀明', '今敏', '汤浅政明', '细田守', '新海诚', '米林宏昌', '罗云奎', '申相玉', '金绮泳', '林权泽', '李沧东', '郭在容', '金基德', '洪尚秀', '姜帝圭', '许秦豪', '朴赞郁', '金知云', '奉俊昊', '罗泓轸', '阮青云', '陈英雄', '潘党迪', '潘礼德', '邱金海', '陈子谦', '陈哲艺', '宗萨钦哲仁波切', '利诺·布罗卡', '拉夫·迪亚兹', '布里兰特·曼多萨', '托尼·裴', '朗斯·尼美毕达', '彭力·云旦拿域安', '韦西·沙赞那庭', '阿彼察邦·韦拉斯哈古', '萨蒂亚吉特·雷伊', '莫利奈·森', '李维克·伽塔克', '纳亚尔·胡赛因', '迈克尔·雷德福', '米拉·奈尔', '拉吉库马尔·希拉尼', '阿素托史·哥瓦力克', '桑托什·斯万', '拉兹·卡普尔', '艾布拉希姆·格勒斯坦', '达瑞许·迈赫尔朱伊', '阿巴斯·基亚罗斯塔米', '莫森·玛克玛尔巴夫', '马基德·马基迪', '贾法·帕纳西', '巴赫曼·戈巴迪', '阿斯哈·法哈蒂', '莎米拉·玛克玛尔巴夫', '汉娜·玛克玛尔巴夫', '埃米尔·拜加津', '尤马兹·古尼', '热哈·埃尔坦', '赛米·卡普拉诺格鲁', '埃敏·阿尔柏', '萨飞·托曼', '阿莫斯·科莱克', '阿莫斯·吉泰', '伊安·瑞克利斯', '伊利亚·苏雷曼', '塞缪尔·毛茨', '阿里·福尔曼', '伊藤·福克斯', '查理·卓别林', '阿尔弗雷德·希区柯克', '迈克尔·鲍威尔', '卡罗尔·里德', '大卫·里恩', '约翰·吉勒明', '尼古拉斯·罗伊格', '肯·洛奇', '雷德利·斯科特', '阿德里安·莱恩', '德里克·贾曼', '迈克·李', '艾伦·帕克', '托尼·斯科特', '安东尼·明格拉', '丹尼·博伊尔', '萨姆·门德斯', '盖·里奇', '克里斯托弗·诺兰', '埃德加·赖特', '约翰·卡尼', '奥古斯特·卢米埃尔', '乔治·梅里埃', '让·谷克多', '让·雷诺阿', '罗伯特·布列松', '威廉·惠勒', '让·维果', '雅克·贝克', '埃里克·侯麦', '克里斯·马克', '阿伦·雷乃', '雅克·里维特', '阿涅斯·瓦尔达', '克劳德·夏布洛尔', '弗朗索瓦·特吕弗', '路易·马勒', '罗曼·波兰斯基', '雅克·贝汉', '吕克·贝松', '莱奥·卡拉克斯', '米歇尔·冈瑞', '克里斯托夫·巴拉蒂', '尤里斯·伊文思', '保罗·范霍文', '劳尔·瑟瓦斯', '香特尔·阿克曼', '弗里兹·朗', '恩斯特·刘别谦', '莱妮·里芬施塔尔', '马克斯·奥菲尔斯', '沃尔克·施隆多夫', '沃尔夫冈·彼德森', '沃纳·赫尔佐格', '维姆·文德斯', '汤姆·提克威', '安杰依·瓦伊达', '克日什托夫·扎努西', '克日什托夫·基耶斯洛夫斯基', '安德烈·祖拉斯基', '薇拉·希季洛娃', '米洛斯·福尔曼', '杨·史云梅耶', '伊利·曼佐', '扬·斯维拉克', '米克洛斯·杨索', '卡罗利·马克', '伊斯特凡·萨博', '贝拉·塔尔', '拉斯洛·奈迈施', '迈克尔·哈内克', '尤里西·塞德尔', '阿兰·泰纳', '弗谢沃罗德·普多夫金', '亚历山大·杜辅仁科', '吉加·维尔托夫', '谢尔盖·爱森斯坦', '列夫·库里肖夫', '米哈伊尔·罗姆', '米哈依尔·卡拉托佐夫', '谢尔盖·格拉西莫夫', '谢尔盖·邦达尔丘克', '格利高利·丘赫莱依', '斯坦尼斯拉夫·罗斯托茨基', '埃利达尔·梁赞诺夫', '安德烈·塔可夫斯基', '安德烈·康查洛夫斯基', '弗拉基米尔·缅绍夫', '尼基塔·米哈尔科夫', '亚历山大·索科洛夫', '安德烈·萨金塞夫', '乔纳斯·梅卡斯', '谢尔盖·帕拉杰诺夫', '埃米尔·库斯图里卡', '霍拉蒂乌·马拉埃雷', '克利斯提·普优', '克里斯蒂安·蒙吉', '卡塔林·米图雷斯库', '弗洛林·谢尔班', '柯内流·波蓝波宇', '拉杜·裘德', '米尔科·曼彻夫斯基', '加布里埃尔·阿克谢', '卡尔森·亨宁', '比利·奥古斯特', '苏珊娜·比尔', '托马斯·温特伯格', '维克多·斯约斯特洛姆', '莫里兹·斯蒂勒', '英格玛·伯格曼', '维尔戈特·斯耶曼', '波·维德伯格', '罗伊·安德森', '拉斯·霍尔斯道姆', '阿基·考里斯马基', '本特·哈默', '埃斯基尔·沃格特', '达格·卡利', '格里莫·哈克纳尔森', '鲁纳·鲁纳森', '罗伯托·罗西里尼', '卢奇诺·维斯康蒂', '米开朗基罗·安东尼奥尼', '费德里科·费里尼', '弗朗西斯科·罗西', '赛尔乔·莱昂内', '马可·贝罗奇奥', '贝纳尔多·贝托鲁奇', '达里奥·阿基多', '罗伯托·贝尼尼', '朱塞佩·托纳多雷', '米开朗基罗·弗兰马汀诺', '保罗·索伦蒂诺', '路易斯·布努埃尔', '卡洛斯·绍拉', '维克多·艾里斯', '比格斯·鲁纳', '佩德罗·阿莫多瓦', '胡里奥·密谭', '佩德罗·科斯塔', '米古尔·戈麦斯', '西奥·安哲罗普洛斯', '米哈利斯·卡科伊亚尼斯', '丹尼斯·阿康特', '大卫·柯南伯格', '詹姆斯·卡梅隆', '盖伊·马丁', '帕特丽夏·罗兹玛', '佛朗索瓦·吉拉德', '布鲁斯·拉布鲁斯', '丹尼斯·维伦纽瓦', '文森佐·纳塔利', '贾森·雷特曼', '泽维尔·多兰', '罗伯特·弗拉哈迪', '迈克尔·柯蒂斯', '维克多·弗莱明', '约翰·福特', '巴斯特·基顿', '霍华德·霍克斯', '弗兰克·卡普拉', '乔治·库克', '茂文·勒鲁瓦', '比利·怀尔德', '约翰·休斯顿', '伊利亚·卡赞', '尼古拉斯·雷', '斯坦利·克雷默', '奥逊·威尔斯', '西德尼·吕美特', '罗伯特·奥特曼', '萨姆·佩金帕', '斯坦利·库布里克', '安迪·沃霍尔', '克林特·伊斯特伍德', '迈克·尼科尔斯', '伍迪·艾伦', '特瑞·吉列姆', '巴瑞·莱文森', '芭芭拉·史翠珊', '马丁·斯科塞斯', '迈克尔·曼', '泰伦斯·马力克', '乔治·卢卡斯', '大卫·林奇', '罗伯·莱纳', '约翰·卡朋特', '史蒂文·斯皮尔伯格', '马丁·布莱斯', '凯瑟琳·毕格罗', '罗伯特·泽米吉斯', '爱德华·兹威克', '吉姆·贾木许', '伊桑·科恩', '罗兰·艾默里奇', '梅尔·吉布森', '斯派克·李', '蒂姆·波顿', '查理·考夫曼', '山姆·雷米', '理查德·林克莱特', '托德·海因斯', '大卫·芬奇', '史蒂文·索德伯格', '昆汀·塔伦蒂诺', '迈克尔·贝', '布莱恩·辛格', '达伦·阿伦诺夫斯基', '韦斯·安德森', '斯派克·琼斯', '索菲亚·科波拉', '达米恩·查泽雷', '埃米利奥·费尔南德斯', '亚历桑德罗·佐杜洛夫斯基', '奥图罗·利普斯坦', '阿方索·卡隆', '卡洛斯·卡雷拉', '卡洛斯·雷加达斯', '米歇尔·弗兰克', '阿玛特·伊斯卡拉特', '温贝托·索洛斯', '费尔南多·佩雷斯', '乔舒华·玛斯顿', '希罗·盖拉', '豪尔赫·圣西内斯', '洛伦佐·维加斯', '克劳迪雅·洛萨', '温伯托·莫罗', '安塞尔莫·杜阿尔特', '鲁伊·古雷拉', '小沃尔特·利马', '格劳贝尔·罗恰', '卡洛斯·迭戈', '费尔南多·梅里尔斯', '沃尔特·塞勒斯', '若泽·帕迪里亚', '亚德里安·卡泰诺', '费尔南多·索拉纳斯', '莱昂纳多·法维奥', '雨果·圣地亚哥', '阿道夫·阿里斯塔里安', '卡洛斯·索林', '艾里西欧·苏比耶拉', '海科特·巴班克', '路易斯·普恩佐', '卢奎西亚·马特尔', '帕布罗·查比罗', '利桑德罗·阿隆索', '达米安·斯兹弗隆', '阿尔多·弗朗西亚', '拉乌·鲁兹', '帕特里克·古兹曼', '米盖尔·里廷', '安德烈斯·伍德', '帕布罗·拉雷恩', '塞巴斯蒂安·席尔瓦', '保罗·考克斯', '彼得·威尔', '乔治·米勒', '吉莉安·阿姆斯特朗', '安娜·库金诺斯', '巴兹·鲁赫曼', '亚历克斯·普罗亚斯', '凯特·休特兰', '亚当·艾略特', '贾斯汀·库泽尔', '简·坎皮恩', '彼得·杰克逊', '尤瑟夫·夏因', '阿托姆·伊戈扬', '乌斯曼·塞姆班', '达雷尔·鲁特', '加文·胡德', '尼尔·布洛姆坎普', '苏莱曼·西塞', '伊德沙·渥德拉戈', '拉契得·波查拉', '阿伯德拉马纳·希萨柯', '苏赫拉布·沙希德·萨利斯', '努里·比格·锡兰', '让·皮埃尔·梅尔维尔', '亚历斯·冯·华麦丹', '雅克·范·多梅尔', '赖纳·维尔纳·法斯宾德', '乔治·威廉·巴布斯特', '约瑟夫·冯·斯登堡', '卡林·皮特·内策尔', '卡尔·西奥多·德莱叶', '拉斯·冯·提尔', '尼古拉斯·温汀·雷弗恩', '维托里奥·德·西卡', '朱塞佩·德·桑蒂斯', '皮埃尔·保罗·帕索里尼', '马可·图利欧·吉欧达纳', '曼努埃尔·德·奥利维拉', '约阿·凯撒·蒙泰罗', '弗朗西斯·福特·科波拉', '布莱恩·德·帕尔玛', '格斯·范·桑特', '保罗·托马斯·安德森', '亚利桑德罗·冈萨雷斯·伊纳里图', '吉尔莫·德尔·托罗', '托马斯·古铁雷兹·阿莱', '阿曼多·罗伯斯·戈多伊', '沃尔特·雨果·克霍里', '内尔森·帕雷拉·德桑托斯', '萨拉赫·阿布·塞义夫', '迪吉布利尔·迪奥普·曼贝提', '瓦基姆·佩德罗·德·安德拉德']
# directors = ['张艺谋','宁浩']
chrome_option = Options()
# chrome_option.add_argument('--headless')
driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe", options=chrome_option)

for director in directors:
	# 设置想要下载的导演 数据集
	# 写CSV文件
	file_name = './' + director + '.csv'
	base_url = 'https://movie.douban.com/subject_search?search_text='+director+'&cat=1002&start='
	# 这豆瓣居然把我IP封了
	# 追加写
	out = open(file_name,'a+', newline='', encoding='utf-8-sig')
	csv_write = csv.writer(out, dialect='excel')
	flags=[]
	# 下载指定页面的数据
	def download(request_url):
		driver.get(request_url)
		time.sleep(1)
		html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
		html = etree.HTML(html)
		# 设置电影名称，导演演员 的XPATH
		movie_lists = html.xpath("/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']")
		name_lists = html.xpath("/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='meta abstract_2']")
		# 获取返回的数据个数
		num = len(movie_lists)
		if num > 15: #第一页会有16条数据
			# 默认第一个不是，所以需要去掉
			movie_lists = movie_lists[1:]
			name_lists = name_lists[1:]
		for (movie, name_list) in zip(movie_lists, name_lists):
			# 会存在数据为空的情况
			if name_list.text is None:
				continue
			# 显示下演员名称
			print(name_list.text)
			names = name_list.text.split('/')
			# 判断导演是否为指定的director
			if names[0].strip() == director and movie.text not in flags:
				# 将第一个字段设置为电影名称
				names[0] = movie.text
				flags.append(movie.text)
				# # 把电影导演的名字也加上
				# names.append(director)
				csv_write.writerow(names)
		print('OK') # 代表这页数据下载成功
		time.sleep(1)
		print(num)
		if num >= 14: #有可能一页会有14个电影
			# 继续下一页
			return True
		else:
			# 没有下一页
			return False

	# 开始的ID为0，每页增加15
	start = 0
	while start<10000: #最多抽取1万部电影
		request_url = base_url + str(start)
		# 下载数据，并返回是否有下一页
		flag = download(request_url)
		if flag:
			start = start + 15
		else:
			break
	out.close()
	print('finished')
	time.sleep(1)



