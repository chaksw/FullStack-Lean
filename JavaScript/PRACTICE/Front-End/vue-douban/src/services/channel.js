export default {
    // async 标记为异步函数
    async getChannels() {
        // 等待获取相应信息
        var resp = await fetch(
            '/x/web-interface/wbi/index/top/feed/rcmd?web_location=1430650&y_num=3&fresh_type=4&feed_version=V8&fresh_idx_1h=1&fetch_row=4&fresh_idx=1&brush=1&homepage_ver=1&ps=12&last_y_num=4&screen=1151-919&seo_info=&last_showlist=av_1156103037,av_1605752098,av_1756067076,av_1006045574,av_1556247479,ad_5614_1656446271,av_1506005824,av_n_1055952084,av_n_1906479803,av_n_1206373743&uniq_id=87293321357&w_rid=2faf0522800f01a5e668aa1e7face476&wts=1721713396',
        );
        // 解析相应体
        console.log(resp)
        console.log(typeof(resp))
        var data = await resp.json();
        console.log(data.data);
        return data.data;
    },
};
