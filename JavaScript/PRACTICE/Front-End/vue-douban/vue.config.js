// vue-cli 配置文件, 90%的配置都是webpack的配置

module.exports = {
    devServer: {
        proxy: {
            // 配置代理
            '/x': {
                // 凡事以 “/x 开头的请求，进行代理
                target: 'https://api.bilibili.com',
            },
            onProxyReq(proxyReq) {
                // add custom header to request
                proxyReq.setHeader('origin', 'https://www.bilibili.com');
                proxyReq.setHeader('referer', 'https://www.bilibili.com/?spm_id_from=333.1365.0.0');
                // or log the req
            },
        },
    },
};
