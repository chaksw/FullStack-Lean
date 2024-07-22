export default {
    // async 标记为异步函数
    async getChannels() {
        // 等待获取相应信息
        var resp = await fetch(
            '/x/web-show/wbi/res/locs?pf=0&ids=3449&w_rid=7c8bb3da94a5bf9cd025549bf4d8d943&wts=1721657399',
        );
        // 解析相应体
        var data = await resp.json();
        console.log(data.data);
        return data.data;
    },
};
