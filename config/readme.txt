1.使用函数def zone(self, field, itemname)
审方工作统计-按机构统计-住院-按机构
审方工作统计-按机构统计-门急诊-按机构
医生处理统计-按机构统计-住院-按机构
医生处理统计-按机构统计-门急诊-按机构
2.使用函数def dept(self, field, itemname)
审方工作统计-按机构统计-住院-按科室
审方工作统计-按机构统计-门急诊-按科室
医生处理统计-按机构统计-住院-按科室
医生处理统计-按机构统计-门急诊-按科室
3.使用函数def doc(self, field, itemname)
审方工作统计-按机构统计-住院-按医生
审方工作统计-按机构统计-门急诊-按医生
医生处理统计-按机构统计-住院-按医生
医生处理统计-按机构统计-门急诊-按医生
4.使用函数def doc_group(self, field, itemname)
审方工作统计-按机构统计-住院-按医疗组
医生处理统计-按机构统计-住院-按医疗组
5.使用函数def ward(self, field, itemname)
审方工作统计-按机构统计-住院-按病区
医生处理统计-按机构统计-住院-按病区
6.
审方工作统计-按药师统计-住院-药师名称
审方工作统计-按药师统计-门诊-药师名称
医生处理统计-按药师统计-住院-药师名称
医生处理统计-按药师统计-门诊-药师名称

审方工作统计-按机构统计
disCount
autoPassCount
autoPassCountRatio      autoPassCount/disCount
timeoutPassCount
timeoutPassCountRatio   timeoutPassCount/disCount
disAuditCount
disAuditCountRatio      disAuditCount/disCount
disAuditPassCount
disAuditPassCountRatio  disAuditPassCount/disAuditCount
disAuditRejecCount
disAuditRejecCountRatio disAuditRejecCount/disAuditCount
auditCount
auditPassCount
auditPassCountRatio     auditPassCount/auditCount
auditRejectCount
auditRejectCountRatio   auditRejectCount/auditCount

审方工作统计-按药师统计
disAuditCount
disAuditPassCount
disAuditPassCountRatio      disAuditPassCount/disAuditCount
disAuditRejecCount
disAuditRejecCountRatio     disAuditPassCount/disAuditCount
auditCount
auditPassCount
auditPassCountRatio         auditPassCount/auditCount
auditRejectCount
auditRejectCountRatio       auditRejectCount/auditCount

医生处理统计
rejectCount
rejectSignCount
rejectSignCountRatio         rejectSignCount/rejectCount
rejectAlterCount
rejectAlterCountRatio        rejectAlterCount/rejectCount
docDealCount
docDealCountRatio            docDealCount/rejectCount
docSignCount
docSignCountRatio            docSignCount/rejectCount
docAlterCount
docAlterCountRatio           docAlterCount/rejectCount
docCancelCount
docCancelCountRatio          docCancelCount/rejectCount





sql中门诊科室格式为：zoneid_deptid

按问题类型统计

/api/v1/sfReport/issueReportByType

"analysisResultType": "抗菌药物诊断超常"
"analysisType": "超常性分析"
"endTime": 1559577599000
"page": 1
"pageSize": 20
"source": "住院"
"startTime": 1557849600000


allGroupNum
rejectGroupNum
rejectGroupRatio
docDoubleSignNum
docDoubleSignRatio
docModifyNum
docModifyRatio

rejectGroupNum/allGroupNum
docDoubleSignNum/rejectGroupNum
docModifyNum/rejectGroupNum


