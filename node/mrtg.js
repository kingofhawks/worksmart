/**
 * Created by user on 2015/12/11.
 */
var jsdom = require("jsdom");
var fs = require("fs");
var jquery = fs.readFileSync("../static/jquery/jquery2.1.4.min.js", "utf-8");
//var traffic = {"http://192.168.153.226:8081/192.168.153.18_37.html":"",
//                "http://192.168.153.226:8081/192.168.153.18_45.html":"",
//                "http://192.168.153.226:8081/192.168.153.15_10.html":"",
//                "http://192.168.153.226:8081/192.168.153.18_46.html":"",
//                "http://192.168.153.226:8081/192.168.153.17_1.html":""}

function traffic(url){
    jsdom.env({
        url: url,
        src: [jquery],
        done: function (err, window) {
            var $ = window.$;
            var status = {'url': url}
            //select second td of tr(class out)
            $("tr.out td:nth-child(2)").each(function (idx) {
                //console.log(idx+" -", $(this).text());
                //capture weekly traffic
                if (idx === 1){
                    status['max'] = $(this).text()
                }
            });
            $("tr.out td:nth-child(3)").each(function (idx) {
                //console.log(idx+" -", $(this).text());
                //capture weekly traffic
                if (idx === 1){
                    //traffic[url] = $(this).text()
                    //console.log(traffic)
                    status['avg'] = $(this).text()
                }
            });
            console.log(status);
        }
    });
}
traffic("http://192.168.153.226:8081/192.168.153.18_37.html")
traffic("http://192.168.153.226:8081/192.168.153.18_45.html")
traffic("http://192.168.153.226:8081/192.168.153.15_10.html")
traffic("http://192.168.153.226:8081/192.168.153.18_46.html")
traffic("http://192.168.153.226:8081/192.168.153.17_1.html")
//for (var url in traffic) {
//    jsdom.env({
//        url: url,
//        src: [jquery],
//        done: function (err, window) {
//            var $ = window.$;
//            //select second td of tr(class out)
//            $("tr.out td:nth-child(2)").each(function (idx) {
//                console.log(idx+" -", $(this).text());
//                //capture weekly traffic
//                if (idx === 1){
//                    traffic[url] = $(this).text()
//                    console.log(traffic)
//                }
//            });
//        }
//    });
//}

