// create xlsx file Moudle
var Excel = require('exceljs');
// http get request
var request = require("sync-request");
// parsing 
var cheerio = require("cheerio");

var filename = 'crawl_saramin.xlsx';
var workbook = new Excel.Workbook();
var worksheet = workbook.addWorksheet('My Sheet');

var url = "http://www.saramin.co.kr/zf_user/jobs/public/list?sort=ud&quick_apply=&search_day=&keyword=&pr_exp_lv%5B%5D=1&up_cd%5B%5D=3";
var request = require('sync-request');
var res = request('GET', url);
var $=cheerio.load(res.getBody());
var postElements = $("table.common_recruit_list tr");

var object= new Object();
object.Name=[];
object.endDate=[];

postElements.each(function() {
    var endDate = $(this).find("td.support_info p.deadlines").text();
    var companyTitle = $(this).find("td.company_nm a").attr("title");
    
    object.Name.push(companyTitle);
    object.endDate.push(endDate);
  });

//console.log(object); // check object

worksheet.columns = [
    { header: '기업명', key: 'id', width: 15 },
    { header: '마감일자', key: 'endDate', width: 15 }
];
 
var i=2;
for(i=2;i<=object.Name.length+2;i++){
    worksheet.getRow(i).getCell(1).value=object.Name[i-2];
    worksheet.getRow(i).getCell(2).value=object.endDate[i-2];
}

workbook.xlsx.writeFile(filename)
    .then(function() {
        console.log("xlsx file created");
        
    });


