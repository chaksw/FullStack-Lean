<template>
    <div>
        <Header></Header>
        <div class="flex items-center justify-center">
            <div class="w-full px-2" style="max-width: 1440px">
                <div id="main" class="bg-primary-300 p-6 text-black">
                    <div class="flex rounded bg-white mx-4 py-6">
                        <div class="mx-6">
                            <div
                                style="
                                    min-height: 259px;
                                    max-height: 300px;
                                    height: 274px;
                                ">
                                <img
                                    class="h-full w-full"
                                    :src="movie.image_url" />
                            </div>
                            <button
                                id="collect"
                                class="bg-blue-500 copy text-white w-full px-4 py-1 mt-2 text-sm rounded border">
                                添加收藏
                            </button>
                        </div>
                        <div id="info" data-movie-id="443">
                            <ul>
                                <li class="text-lg font-semibold">
                                    {{ movie.movie_name }} ({{
                                        movie.release_year
                                    }})
                                </li>
                                <li>导演: {{ movie.director }}</li>
                                <li>编剧: {{ movie.scriptwriter }}</li>
                                <li>主演: {{ movie.actors }}</li>
                                <li>语言: {{ movie.language }}</li>
                                <li>首播: {{ movie.release_date }}</li>
                                <li>集数/时长: {{ movie.duration }}</li>
                                <li>类型: {{ movie.types }}</li>
                                <li>
                                    制片国家/地区:
                                    <span>{{
                                        movie.region === 1
                                            ? "中国大陆"
                                            : movie.region === 2
                                            ? "中国香港"
                                            : movie.region === 3
                                            ? "中国台湾"
                                            : movie.region === 4
                                            ? "美国"
                                            : movie.region === 5
                                            ? "韩国"
                                            : movie.region === 6
                                            ? "日本"
                                            : "其他"
                                    }}</span>
                                </li>
                                <li>又名: {{ movie.alternate_name }}</li>
                                <li>豆瓣评分: {{ movie.rate }}</li>
                            </ul>
                        </div>
                    </div>
                    <div class="rounded bg-white mx-4 my-4 py-6">
                        <div class="px-6">
                            <h1 class="text-lg mb-6 font-semibold">简介</h1>
                            <p>
                                <!-- {{ movie.review }} -->
                            </p>
                        </div>
                    </div>
                    <div
                        id="download_info"
                        class="rounded bg-white mx-4 mt-4 py-6">
                        <h1 class="text-lg mb-6 font-semibold px-6">
                            网盘地址
                        </h1>
                        <ul v-if="movie.download_info" class="px-6">
                            <li>
                                {{ movie.download_info }}
                            </li>
                            <!-- 阿里云盘: http://www.aliyunpan.com 提取码:99999 -->
                            <!-- 百度网盘:http://www.baidu.com 提取码:8888 -->
                        </ul>
                        <ul v-else class="px-6">
                            暂无网盘信息
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <Footer></Footer>
    </div>
</template>

<script>
import Footer from "@/components/Footer.vue";
import Header from "@/components/Header.vue";
import axios from "axios";

export default {
    name: "MovieDetail",
    data: () => {
        return {
            movie: {},
        };
    },
    components: {
        Header,
        Footer,
    },
    mounted() {
        this.getMovieInfo();
    },
    methods: {
        // Vue Router 提供的 $route 对象中的 params。如果 URL 路径定义中包含了 :id 参数（例如 /movie/:id），则 this.$route.params.id 会获取到当前电影的 ID 值。
        getMovieInfo: function () {
            axios
                .get("/api/movie/" + this.$route.params.id)
                .then((response) => (this.movie = response.data))
                .catch((error) => {
                    console.log(error);
                });
        },
    },
};
</script>

<style></style>
