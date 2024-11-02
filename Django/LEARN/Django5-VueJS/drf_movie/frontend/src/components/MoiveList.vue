<template>
    <div>
        <div class="flex items-center justify-center">
            <div class="w-full px-2" style="max-width: 1440px">
                <div
                    id="movie-list"
                    class="p-2 grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
                    <div
                        class="movie"
                        v-for="movie in info.results"
                        :key="movie.id">
                        <a :href="'/movie/' + movie.id">
                            <div class="relative">
                                <div
                                    class=""
                                    style="
                                        min-height: 259px;
                                        max-height: 300px;
                                        height: 274px;
                                    ">
                                    <img
                                        class="rounded h-full w-full"
                                        :src="movie.image_url"
                                        alt=""
                                        crossorigin="anonymous" />
                                    <div
                                        class="rounded absolute top-0 bg-purple-600 px-1 text-sm">
                                        {{ movie.is_top ? "置顶" : "" }}
                                    </div>
                                    <div
                                        class="rounded absolute bottom-0 right-0 bg-blue-500 px-1 text-sm">
                                        {{
                                            movie.quality === 1
                                                ? "720p"
                                                : movie.quality === 2
                                                ? "1080p"
                                                : "4k"
                                        }}
                                    </div>
                                </div>
                            </div>
                        </a>
                        <p>{{ movie.movie_name }} ({{ movie.release_year }})</p>
                        <p class="text-sm text-primary-200">
                            {{ movie.language }}
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <!-- 添加Page组件，并将info数据作为props传递给Page组件 -->
        <Page :info="info"></Page>
        <!-- <Page :info="info"></Page> -->
    </div>
</template>

<script>
import axios from "axios";
import Page from "./Page.vue";

export default {
    name: "MovieList",
    data: () => {
        return {
            info: "",
        };
    },
    components: {
        Page,
    },
    mounted() {
        // 在 mounted 时自动调用
        this.getMovieData();
    },
    methods: {
        getMovieData: function () {
            // 基础 api
            let url = "/api/movie";
            // 获取路由 page 信息
            const page = Number(this.$route.query.page);
            // 获取路由 search 的参数
            const search = this.$route.query.search;
            // 获取路由 category id 参数
            const category_id = Number(this.$route.query.category_id);
            // 获取路由 region 参数
            const region = Number(this.$route.query.region);
            // 将获取到的参数全部加入到 URLSearchParams 对象中
            const params = new URLSearchParams();
            if (page) {
                params.append("page", page);
            }
            if (search) {
                params.append("movie_name", search);
            }
            if (category_id) {
                params.append("category_id", category_id);
            }
            if (region) {
                params.append("region", region);
            }
            // // 组合含 page 的 url
            // if (!isNaN(page) && page !== 0) {
            //     url = url + "/?page=" + page;
            // }
            // 组合 url
            // 组合后的 url 为如： /api/movie?page=2&movie_name=%E6%88%91%E7%9A%84
            url = url + "?" + params.toString();
            console.log(url);
            // 发送 axios GET 请求
            axios
                .get(url)
                .then((response) => (this.info = response.data))
                .catch((error) => {
                    console.log("error", error);
                });
        },
    },
    watch: {
        // 监听路由变化
        $route() {
            // 使用 watch: { $route() { ... } } 可以监听当前路由对象 $route 的变化。当 URL 变化（包括路径、查询参数、哈希等）时，$route 变化触发 watch 回调，从而执行相关代码。
            // 当 Page 组件中调用的 goToPage(), 会将 $route.query 中的 page 参数设置为当前的 page 变量值， 而这一变化会被 watch() $route 所捕捉，进而执行 getMovieData 函数，getMovieData 内部会有已变化的新 page 参数进行数据请求，从而实现基于page更新的页面跳转。
            this.getMovieData();
        },
    },
};
</script>
