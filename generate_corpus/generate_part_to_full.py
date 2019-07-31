#!/usr/bin/env python
# -*-coding=utf-8-*-

import os

industry_list = ['农业', '林业', '畜牧业', '渔业', '农和林和牧和渔服务业', '煤炭开采和洗选业', '石油和天然气开采业', '黑色金属矿采选业', '有色金属矿采选业', '非金属矿采选业',
                 '开采辅助活动', '农副食品加工业', '食品制造业', '酒和饮料和精制茶制造业', '纺织业', '纺织服装和服饰业', '皮革和毛皮和羽毛及其制品和制鞋业',
                 '木材加工和木和竹和藤和棕和草制品业', '家具制造业', '造纸和纸制品业', '印刷和记录媒介复制业', '文教和工美和体育和娱乐用品制造业', '石油加工和炼焦和核燃料加工业',
                 '化学原料和化学制品制造业', '医药制造业', '化学纤维制造业', '橡胶和塑料制品业', '非金属矿物制品业', '黑色金属冶炼和压延加工业', '有色金属冶炼和压延加工业', '金属制品业',
                 '通用设备制造业', '专用设备制造业', '汽车制造业', '铁路和船舶和航空航天和其他运输设备制造业', '电气机械和器材制造业', '计算机和通信和其他电子设备制造业', '仪器仪表制造业',
                 '其他制造业', '废弃资源综合利用业', '电力和热力生产和供应业', '燃气生产和供应业', '水的生产和供应业', '房屋建筑业', '土木工程建筑业', '建筑安装业', '建筑装饰和其他建筑业',
                 '批发业', '零售业', '铁路运输业', '道路运输业', '水上运输业', '航空运输业', '装卸搬运和运输代理业', '仓储业', '邮政业', '住宿业', '餐饮业',
                 '电信和广播电视和卫星传输服务', '互联网和相关服务', '软件和信息技术服务业', '货币金融服务', '资本市场服务', '保险业', '其他金融业', '房地产业', '租赁业', '商务服务业',
                 '研究和试验发展', '专业技术服务业', '科技推广和应用服务业', '生态保护和环境治理业', '公共设施管理业', '机动车和电子产品和日用产品修理业', '教育', '卫生', '新闻和出版业',
                 '广播和电视和电影和影视录音制作业', '文化艺术业', '体育', '综合']

conception_list = ['MSCI概念', '一线龙头', '可转债', '国家队', '外资并购(国际板)', '融资融券', '证金概念', '举牌', '增持', '央企', '深圳前海新区', '特色小镇', '股权激励', '行业龙头',
                   '装配式建筑', '质押式回购', 'PPP', '特斯拉', '环保概念', '二线龙头', '小盘成长', '广东国资改革', '粤港澳大湾区', '云计算', '房屋租赁', '涉矿', '网络游戏', '股权转让',
                   '重组', '高送转概念', '高铁', '军民融合', '创投', '锂电池', '借壳上市', '装饰园林', '粤港澳自贸区', '建筑节能', '新材料', '新能源', '触摸屏', '智能电视', '共享单车',
                   '一带一路', '员工持股', '雄安新区', '3D传感', '智能电网', '绿色节能照明', '白马股', '智慧医疗', '参股金融', '垃圾发电', '核能核电', '风力发电', '国资改革', 'ST概念',
                   '在线教育', '最小市值', '互联网营销', '文化传媒概念', 'LNG', '可燃冰', '高端装备制造', 'OLED', '金控平台', '猪', '苹果', '虚拟现实', '太阳能发电', '卫星导航', '电子商务',
                   '电子竞技', '油气改革', '智慧农业', '智能物流', '4G', '5G', 'IPV6', '去IOE', '宽带提速', '无线充电', '智慧城市', '智能家居', '移动互联网', '移动支付', '第三方支付',
                   '芯片国产化', '抗癌', '禽流感', '三沙', '国企混改', '通用航空', '太赫兹', '智能汽车', '健康中国', '养老产业', '民营医院', 'CDM项目', '三网融合', '京津冀一体化', '丝绸之路',
                   '新疆区域振兴', '物联网', '机器人', '燃料电池', '充电桩', '大央企重组', '新能源汽车', '特高压', '能源互联网', '小金属', '黄金珠宝', '工业4.0', '债转股', '石墨烯', '蓝宝石',
                   '金融改革', '中日韩自贸区', 'O2O', '跨境电商', '长吉图板块', '打板', '稀土永磁', '医药电商', '基因检测', '生物疫苗', '海南旅游岛', '互联网金融', '保底增持', '360概念',
                   '新型煤化工', '高校', '北部湾自贸区', '鸡', '冷链物流', '地热能', '新三板', '量子通信', '钛白粉', '航母', 'PM2.5', '体育', '共享汽车', '乙醇汽油', '尾气治理', '福建自贸区',
                   '赛马', '维生素', '污水处理', '海绵城市', '合同能源管理', '职业教育', '大数据', '土地流转', '页岩气和煤层气', '民营银行', '3D打印', '煤电重组', '智能穿戴', '超级电容',
                   '天津自贸区', '智能交通', '浦东新区', 'IP流量变现', '征信', '无人机', '安防监控', '生物育种', '动漫', '西藏振兴', '新零售', '钢结构', '在线旅游', '舟山新区', '移动互联网入口',
                   '移动转售', '网络彩票', '中朝经济特区', '网红经济', '精准扶贫', '核高基', '人工智能', '网络安全', '传感器', '小程序', '智能IC卡', '中小创蓝筹', '汽车后市场', '食品安全',
                   '长江经济带', '染料', '水利水电建设', '区块链', '二胎政策', '迪士尼', '生物识别', '美丽中国', '油气管网升级', '上海自贸区', '上海国资改革', '次新股', '沪股通50', '上海本地重组', '新型城镇化']

low_frequency_index = {'股票代码': 'code', '最新日期': 'date', '多头排列': 'maLong',
                       '5日均线上穿10日均线': 'maCrossAbove_5_10',
'5日均线上穿20日均线': 'maCrossAbove_5_20', '收盘价上探5日均线': 'priceBreak_5', '收盘价上探10日均线': 'priceBreak_10',
'收盘价回踩10日均线': 'priceBack_10', '收盘价回踩20日均线': 'priceBack_20', 'KDJ金叉': 'kdjGoldenCross', 'KDJ死叉': 'kdjDeadCross',
'KDJ高位金叉': 'kdjHighGoldenCross', 'KDJ低位金叉': 'kdjLowGoldenCross', 'KDJ高位死叉': 'kdjHighDeadCross',
'KDJ低位死叉': 'kdjLowDeadCross', '布林通道开口变大': 'bollGapIncrease', '布林通道开口变小': 'bollGapDecrease',
'收盘价上穿BOLL中轨': 'bollCrossAboveMiddleBand', '收盘价上破BOLL上轨': 'bollCrossAboveUpperBand',
'收盘价下破BOLL中轨': 'bollCrossBelowMiddleBand', '收盘价下破BOLL下轨': 'bollCrossBelowLowBand', 'MACD金叉': 'macdGoldenCross',
'MACD死叉': 'macdDeadCross', 'MACD顶背离': 'macdBullishDivergences', 'MACD底背离': 'macdBearishDivergences',
'MACD零轴以上金叉': 'macdUpZeroGo ldenCross', 'MACD零轴以下金叉': 'macdDownZeroGoldenCross', 'MACD零轴以上死叉': 'macdUpZeroDeadCross',
'MACD零轴以下死叉': 'macdDownZeroDeadCross', 'MACD逐步放大': 'macdEnlarge', 'MACD逐步减小': 'macdDecrease', '缩量': 'volumeAtrophy',
'温和放量': 'volumeModerateIncrease', '明显放量': 'volumeObviousIncrease', '巨量放量': 'volumeHugeIncrease',
'天量': 'volumeGodIncrease', '涨跌停标记': 'ltm', 'beta值': 'beta', '空头排列': 'maShort', '均线粘合': 'maBond',
'5日均线连续上涨X天': 'ma5IncreaseX', '收盘价回踩5日均线': 'priceBack_5', '10日均线连续上涨X天': 'ma10IncreaseX',
'20日均线连续上涨X天': 'ma20IncreaseX', '收盘价上探20日均线': 'priceBreak_20', '60日均线连续上涨X天': 'ma60IncreaseX',
'收盘价上探60日均线': 'priceBreak_60', '收盘价回踩60日均线': 'priceBack_60', 'SAR由红转绿': 'sarGreenToRed', 'SAR由绿转红': 'sarRedToGreen',
'SAR持续X日红线': 'sarRedX', 'SAR持续X日绿线': 'sarGreenX', 'KDJ超买': 'kdjOverBuy', 'KDJ超卖': 'kdjOverSell',
'上穿BOLL上轨': 'bollCrossAboveLowBand', '下穿BOLL上轨': 'bollCrossBelowUpperBand', 'RSI超买': 'rsiOverBuy',
'RSI超卖': 'rsiOverSell', 'RSI超买反转': 'rsiBuyToSell', 'RSI超卖反转': 'rsiSellToBuy', 'RSI由底部上升到50以上': 'rsiUpAbove50',
'RSI由顶部下穿到50以下': 'rsiDownBelow50', 'WR超卖': 'wrOverSell', 'WR超买': 'wrOverBuy', 'WR指标上穿50': 'wrUpAbove50',
'WR指标下穿50': 'wrDownBelow50', 'WR超卖反转': 'wrBuyToSell', 'WR超买反转': 'wrSellToBuy', 'PDI上穿MDI': 'pdiUpCrossMdi',
'PDI高于MDI': 'pdiAboveMdi', 'PDI低于MDI': 'pdiBelowMdi', 'ADX高位拐向': 'adxHighToLow', 'ADX20以下': 'adxBelow20',
'PSY高于75': 'psyAbove75', 'PSY低于25': 'psyBelow25', 'PSY高位区间回落75以下': 'psyHighToLow75',
'PSY低位区间反弹25以上': 'psyLowToHigh25', 'ADTM高于0.5': 'adtmAboveP5', 'ADTM低于-0.5': 'adtmAboveN5',
'ADTM-0.5以下金叉': 'adtmGoldenCross', 'ADTM0.5以上死叉': 'adtmDeadCross', 'DMA金叉': 'dmaGoldenCross', 'DMA死叉': 'dmaDeadCross',
'DMA零轴以上金叉': 'dmaUpZeroGoldenCross', 'DMA零轴以下金叉': 'dmaDownZeroGoldenCross', 'ROC超买区间': 'rocOverBuy',
'ROC超卖区间': 'rocOverSell', 'ROC零轴以上金叉': 'rocUpZeroGoldenCross', 'ROC零轴以下金叉': 'rocDownZeroGoldenCross',
'BIAS-12零轴以下': 'biasBelow0', 'BIAS-12零轴以上': 'biasUpper0', 'BIAS正向乖离': 'biasToPositive', 'BIAS负向乖离': 'biasToNegative',
'BIAS-24日线上穿BIAS-6日线': 'bias24UpTo6', 'BIAS-6日线下穿BIAS-24日线': 'bias24DownTo6', 'ASI与10日均线金叉': 'asiMA10GoldenCross',
'ASI与10日均线死叉': 'asiMA10DeadCross', 'ASI突破前次高点': 'asiBreakPreHigh', 'ASI跌破前次低点': 'asiBreakPreLow',
'WVAD上穿零轴': 'wvadUpCrossZero', 'WVAD下穿零轴': 'wvadDownCrossZero', 'WVAD0轴以上金叉': 'wvadUpZeroGoldCross',
'WVAD0轴以下金叉': 'wvadDownZeroGoldCross', 'WVAD零轴以上死叉': 'wvadUpZeroDeadCross', 'WVAD0轴以上死叉': 'wvadDownZeroDeadCross',
'OBV新高': 'obvNewHigh', 'OBV低点': 'obvNewLow', 'OBV顶背离': 'obvBullishDivergences', 'OBV底背离': 'obvBearishDivergences',
'MTM上穿MTMMA': 'mtmUpCrossMtmma', 'MTM下穿MTMMA': 'mtmDownCrossMtmma', 'MTM股价高位背离': 'mtmBullishDivergences',
'MTM股价低位背离': 'mtmBearishDivergences', 'MTM和股价低位上升': 'mtmCloseLowUp', 'MTM和股价高位下降': 'mtmCloseHighDown',
'CR小于50': 'crLt50', 'CR大于400': 'crGt400', 'CR高位下穿CRMAC10日均线': 'crHighPosDownCrossMa10',
'CR连续上穿4根均线': 'crUpCrossFourMa', 'CR回落到4根均线以下': 'crDownCrossFourMa', 'EXPMA向上交叉': 'expmaUpCross',
'EXPMA向下交叉': 'expmaDownCross', 'EXP1大于EXP2': 'exp1GtExp2', 'EXP1小于EXP2': 'exp1LtExp2',
'EXPMA多头进攻': 'expmaMaLongSpeedUp', 'EXPMA空头进攻': 'expmaMaShortSpeedUp', 'EXPMA多头回撤': 'expmaMaLongTop',
'EXPMA空头回撤': 'expmaMaShortTop', '收盘价自上向下穿越BBI': 'closeDownCrossBbi', '收盘价自下向上穿越BBI': 'closeUpCrossBbi',
'股价高于BBI': 'closeGtBbi', '股价低于BBI': 'closeLtBbi', '收盘价触及上顶边': 'closeTouchXtTop', '收盘价触及下底边': 'closeTouchXtBottom',
'收盘价上穿箱体顶边': 'closeUpCrossXtTop', '收盘价高于箱体顶边': 'closeGtXtTop', '收盘价回返箱体之内': 'closeBackIntoXt',
'收盘价下穿箱体底边': 'closeDownCrossXtBottom', 'A线上穿J线': 'aUpCrossJ', 'A线下穿J线': 'aDownCrossJ', 'A线位于J线之上': 'aAboveJ',
'A线位于J线之下': 'aBelowJ', '收盘价高于A线，A线高于J线': 'closeGtAandAGtJ', '收盘价低于A线，A线低于J线': 'closeLtAandALtJ',
'瀑布线多头发散': 'pubuMaLong', '瀑布线空头发散': 'pubuMaShort', '瀑布线顶部背离': 'pubuBullishDivergences',
'瀑布线底部收敛': 'pubuBearishDivergences', '瀑布线无序盘整': 'pubuDull', '单日股价低位上穿瀑布线': 'closeUpCrossPubu',
'单日股价高位下穿瀑布线': 'closeDownCrossPubu', '箱体突破形态': 'xtBreak', 'DMA零轴以上X次金叉': 'dmaUpZeroGoldenCrossX',
'DMA零轴以下X次金叉': 'dmaDownZeroGoldenCrossX', '启明星': 'morningStar', '黄昏星': 'eveningStar', '高开大阴线': 'leaveBigline',
'低开大阳线': 'lineOpened', '三连阴': 'threeYin', '三连阳': 'threeYang', '四周突破法则': 'breakFourRules', '跳空缺口高开': 'breakAwayHigh',
'跳空缺口低开': 'breakAwayLow', '乌云盖顶形态': 'darkcloudOverhead', '平台整理': 'platformFinishing', '强势整理': 'strongArrangement',
'V形反转': 'vReverse', 'U形反转': 'uReverse', 'N字上升形态': 'nRise', '创建时间': 'create_time', '更新时间': 'update_time',
 '市盈率': 'pe', '市净率': 'pb', '市销率': 'ps', '动态PE（TTM）': 'pe_ttm', '动态PS（TTM）': 'ps_ttm',
'经营市现率TTM': 'popcf', '总市值': 'totalmarketvalue', '流通市值': 'tfc', '总股本': 'totals', '股息率': 'dpr',
'销售净利率': 'gross_profit_rate', '经营利润率': 'opm', '净利润率': 'npm', '净利润': 'net_profits', '营业收入增长率': 'revg',
'净利润增长率': 'nprg', '总资产收益率': 'roaa', '净资产收益率': 'roe', '资本回报率': 'roic', '每股收益增长率': 'epsg', '基本每股收益': 'eps',
'每股未分配利润': 'perundp', '每股息税前利润': 'ebits', '每股净资产': 'bvps', '每股盈余公积': 'srs', '每股股利': 'per_st_profit', '负债权益比': 'lde',
'归属于母公司的所有者权益': 'ytototalcap', '权益乘数': 'em', '归属母公司股东权益增长率': 'eamig', '每股经营现金流': 'opcfs',
'每股公积金': 'reservedPerShare', '每股现金流': 'epcf', '收盘价': 'close', 'A股流通股本': 'ashares_trade', '营业总收入': 'total_revenue',
'营业利润': 'operation_profit', '经营性现金流净值': 'cfo', '净利润现金含量': 'cfo_netincome', 'DateTime)': 'ipo_date',
'单季度归母净利润增长率（TTM）': 's_qfa_yoynetprofit', '现金比率': 'cashratio', '销售现金比率': 'cf_sales', '经营现金净流量对销售收入比率': 'cf_sales',
'应收账款周转率': 'arturnover', '存货周转率': 'inventory_turnover', '流动资产周转率': 'currentasset_turnover',
'营业税金及附加': 'business_taxes', '营业总成本': 'total_operating_costs', '营业成本': 'operating_costs', '销售费用': 'sales_expenses',
'财务费用': 'net_financial_expenses', '利润总额': 'pre_tax_profit', '税前利润': 'pre_tax_profit', '税后利润': 'af_tax_profit',
'投资活动产生的现金流量净额': 'incf', '支付给职工以及为职工支付的现金': 'cpte', '筹资活动产生的现金流量净额': 'fncf', '期末现金及现金等价物余额': 'cate',
'货币资金': 'cash_equivalents', '交易性金融资产': 'financial_assets_at_fair_value', '应收账款': 'accounts_receivable',
'存货': 'inventories', '流动资产合计': 'total_current_assets', '固定资产': 'fixed_property', '无形资产': 'intangible_assets',
'商誉': 'goodwill', '资产总计/资产总额': 'total_assets', '资本公积金': 'capital_reserve', '盈余公积金': 'surplus_reserve',
'未分配利润': 'retained_earnings', '股东权益合计': 'total_equity', '投资性房地产': 'invest_real_estate',
'非流动资产合计': 'tot_non_cur_assets', '流动负债合计': 'tot_cur_liab', '专项应付款': 'specific_item_payable',
'非流动负债合计': 'tot_non_cur_liab', '负债合计': 'tot_liab', '专项储备': 'special_rsrv', '所有者权益合计': 'tot_shrhldr_eqy_incl_min_int',
'营业收入': 'oper_rev', '管理费用': 'less_gerl_admin_exp', '所得税费用': 'inc_tax', '销售商品和提供劳务收到的现金': 'cash_recp_sg_and_rs',
'收到其他与经营活动有关的现金': 'other_cash_recp_ral_oper_act', '经营活动现金流入小计': 'stot_cash_inflows_oper_act',
'经营活动现金流出小计': 'stot_cash_outflows_oper_act', '经营活动产生的现金流量净额': 'net_cash_flows_oper_act',
'投资活动现金流入小计': 'stot_cash_inflows_inv_act', '投资活动现金流出小计': 'stot_cash_outflows_inv_act',
'筹资活动现金流入小计': 'stot_cash_inflows_fnc_act', '筹资活动现金流出小计': 'stot_cash_outflows_fnc_act',
'现金及现金等价物净增加额': 'net_incr_cash_cash_equ', '销售毛利率': 's_fa_grossprofitmargin',
'每股现金流量净额': 's_fa_cfps', '应收账款周转天数': 's_fa_arturndays',
'存货周转天数': 's_fa_invturndays',  '固定资产周转率': 's_fa_faturn', '总资产周转率': 's_fa_assetsturn',
'流动比率': 's_fa_current', '速动比率': 's_fa_quick', '产权比率': 's_fa_debttoequity', '利息保障倍数': 's_fa_ebittointerest',
'无形资产比率': 'intangible_per_total', '固定资产比率': 'fixed_per_total', '非流动资产比率': 'non_cur_per_total',
'营运资本（万元）': 'op_capital', '股东权益比率': 'shareholder_per_assets', '资本化比率': 'capitalized_ratio',
'股东权益与固定资产比率': 'equity_per_fixed', '净资产增长率': 's_fa_yoy_equity', '营业利润增长率': 's_fa_yoyop',
'负债和所有者权益总计': 'tot_liab_shrhldr_eqy', '成本费用利润率': 'profit_per_cost', '成本费用净利润率': 'net_profit_per_cost',
'现金流动负债比率': 'cash_per_cur_liab', '有形净值债务率': 'tangible_per_tot_liab', '偿债保障比率': 'tot_liab_net_ocf',
'资产负债比率': 'asset_per_liab', '长期负债比率': 'long_liab_per_asset',
'基本收益率': 'ebit_per_avg_tot_asset', '资产利润率': 'tot_profit_per_avg_tot_asset', '股利支付率': 'div_payout_ratio',
'收益留存率': 'retention_ratio', '总资产增长率': 'tot_asset_growth_rate', '可持续增长率': 'sustainable_growth_rate',
'资本负债比率': 'liab_per_equity', '净现金流量结构分析': 'ocf_per_tot_cf', '（到期债务）本息偿付比率': 'principal_interest_repayment_ratio',
'应收票据': 'notes_rcv', '预付款项': 'prepay', '其他应收款': 'oth_rcv', '一年内到期的非流动资产': 'non_cur_assets_due_within_1y',
'其他流动资产': 'oth_cur_assets', '长期股权投资': 'long_term_eqy_invest', '长期应收款': 'long_term_rec', '开发支出': 'r_and_d_costs',
'短期借款': 'st_borrow', '应付票据': 'notes_payable', '应付账款': 'acct_payable', '预收款项': 'adv_from_cust',
'应付职工薪酬': 'empl_ben_payable', '应交税费': 'taxes_surcharges_payable', '应付利息': 'int_payable', '应付股利': 'dvd_payable',
'其他应付款': 'oth_payable', '一年内到期的非流动负债': 'non_cur_liab_due_within_1y', '其他流动负债': 'oth_cur_liab', '长期借款': 'lt_borrow',
'应付债券': 'bonds_payable', '长期应付款': 'lt_payable', '长期应付职工薪酬': 'lt_payroll_payable', '股本': 'cap_stk',
'其他综合收益': 'other_comp_income', '购买商品和接受劳务支付的现金': 'cash_pay_goods_purch_serv_rec', '支付的各项税费': 'pay_all_typ_tax',
'支付其他与经营活动有关的现金': 'other_cash_pay_ral_oper_act', '收回投资收到的现金': 'cash_recp_disp_withdrwl_invest',
'取得投资收益收到的现金': 'cash_recp_return_invest', '购建固定资产和无形资产和其他长期资产支付的现金': 'cash_pay_acq_const_fiolta',
'投资支付的现金': 'cash_paid_invest', '吸收投资收到的现金': 'cash_recp_cap_contrib', '取得借款收到的现金': 'cash_recp_borrow',
'发行债券收到的现金': 'proc_issue_bonds', '偿还债务支付的现金': 'cash_prepay_amt_borr',
'分配股利和利润或偿付利息支付的现金': 'cash_pay_dist_dpcp_int_exp', '期初现金及现金等价物余额': 'cash_cash_equ_beg_period',
'可供出售金融资产': 'fin_assets_avail_for_sale', '资产减值损失': 'impairtog',
'营业外收入': 'plus_non_oper_rev', '营业外支出': 'less_non_oper_exp'}


def test_1(path, bk, n):
    __f = open(path, 'w+', encoding='utf-8')
    count = 0
    for i in range(len(bk)):
        print(i)
        print(bk[i])
        if len(bk[i]) <= 2:
            if count % n == 0:
                __f.write("\n'': '{}', ".format(bk[i]))
            else:
                __f.write("'': '{}', ".format(bk[i]))
            count += 1
        elif 5 > len(bk[i]) >= 3:
            if count % n == 0:
                count += 2
                if n == 2:
                    __f.write("\n'': '{}', ".format(bk[i]))
                    __f.write("'': '{}', ".format(bk[i]))
                elif n == 3:
                    __f.write("\n'': '{}', ".format(bk[i]))
                    __f.write("'': '{}', ".format(bk[i]))
            elif count % n == 1:
                count += 2
                if n == 2:
                    __f.write("'': '{}', ".format(bk[i]))
                    __f.write("\n'': '{}', ".format(bk[i]))
                elif n == 3:
                    __f.write("'': '{}', ".format(bk[i]))
                    __f.write("'': '{}', ".format(bk[i]))
        else:
            if count % n == 0:
                count += 4
                if n == 2:
                    __f.write("\n'': '{}', ".format(bk[i]))
                    __f.write("'': '{}', ".format(bk[i]))
                    __f.write("\n'': '{}', ".format(bk[i]))
                    __f.write("'': '{}', ".format(bk[i]))
                elif n == 3:
                    __f.write("\n'': '{}', ".format(bk[i]))
                    __f.write("'': '{}', ".format(bk[i]))
                    __f.write("'': '{}', ".format(bk[i]))
                    __f.write("\n'': '{}', ".format(bk[i]))
            elif count % n == 1:
                count += 4
                if n == 2:
                    __f.write("'': '{}', ".format(bk[i]))
                    __f.write("\n'': '{}', ".format(bk[i]))
                    __f.write("'': '{}', ".format(bk[i]))
                    __f.write("\n'': '{}', ".format(bk[i]))
                elif n == 3:
                    __f.write("'': '{}', ".format(bk[i]))
                    __f.write("'': '{}', ".format(bk[i]))
                    __f.write("\n'': '{}', ".format(bk[i]))
                    __f.write("'': '{}', ".format(bk[i]))
    __f.close()


def test_2():
    __f = open('./data/conception_part', 'w', encoding='utf-8')
    for i in range(len(conception_list)):
        if i % 3 == 0:
            __f.write("\n'': '{}', ".format(conception_list[i]))
            __f.write("'': '{}', ".format(conception_list[i]))
            __f.write("'': '{}', ".format(conception_list[i]))
        else:
            __f.write("'': '{}', ".format(conception_list[i]))
    __f.close()


def test_3():
    """
    dict.keys可以迭代取出数据，可以用len得到长度，但是不是列表，不能用下标访问
    :return:
    """
    __f = open('./data/index_part', 'w', encoding='utf-8')
    # print(len(low_frequency_index.keys()))
    # for i in low_frequency_index.keys():
    #     print(i)
    index = list(low_frequency_index.keys())
    # print(index)
    for i in range(len(index)):
        __f.write("\n'': '{}', ".format(index[i]))
        __f.write("'': '{}', ".format(index[i]))
        __f.write("'': '{}', ".format(index[i]))
    __f.close()
test_3()

project_path = os.path.dirname(__file__)
print(project_path)
# 注意data前面不要加\或者
path_conception = os.path.join(project_path, 'data\conception_part')
print(path_conception)
# test_1(path=path_conception, bk=conception_list, n=3)

path_index = os.path.join(project_path, 'data\index_part')
index_list = list(low_frequency_index.keys())
print(index_list)
# test_1(path=path_index, bk=index_list, n=3)
