# 1. Vite + VueJs + Vue-Router4 + ElementPlus + Tailwinds

## 1.1. Vite + VueJs3 Setup

1. Create vite + vue3 project
```bash
npm create vite@latest
```
2. Dependencies installation

```bash
npm i
```

## 1.2. Vite + VueJs3 + Vue-Router4 Configuration

> see FullStack-Lean\JavaScript\PRACTICE\Front-End\Vue-Practice\vue-router4 for usage of vue-router


1. Vue-Route4 installation
```bash
npm install vue-router@4 --save
```

2. Router prese: mapping of `@` to `../src` (only valid with `import` command)
```js
// in vite.config.js (created in npm create vite@latest)

...
import path from "path";

// https://vite.dev/config/
export default defineConfig({
	...
	resolve: {
		alias: {
			"@": path.resolve(__dirname, "src"),
		},
	},
});

```

```js
// create a new jsconfig.json file
{
    "compilerOptions": {
        "baseUrl": ".",
        "paths": {
            "@/*": [
                "src/*"
            ]
        }
    }
}
```

3. Router setup
   1. create folder `router` and file `index.js` under `src/`
   2. In `index.js` create `routes` as url objects and `router` as route rule
```js
// router -> index.js
import { createRouter, createWebHistory } from "vue-router";

const routes = [
	{
		path: "/",
		component: () => import("@/views/index.vue"),
	},
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default router;

```

4. import router and use in `App.vue`
   1. import router in main.js
```js
// main.js
import { createApp } from "vue";
import router from "./router"; // import router
import App from "./App.vue";

const app = createApp(App);

app.use(router) // use router
app.mount("#app");

```
   2. use router configuration in `App.vue` by calling <router-view/> 
```html
<!-- App.vue -->
 <script setup></script>

<template>
	<router-view />
</template>

<style scoped></style>

```

## 1.3. ElementPlus + TailwindCss
1. Installation
   1. Installation of ElementPlus
```bash
npm install element-plus --save 
```
   2. Installation of tailwindcss in vite project
```bash
npm install -D tailwindcss postcss autoprefixer # Install tailwindcss and its peer dependencies
npx tailwindcss init -p # generate tailwind.config.js and postcss.config.js files.
```
2. Configuration of tailwind.config.js and postcss.config.js files
```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
	content: ["./index.html", "./src/**/*.{vue,ts,js,jsx,tsx,html}"],
	theme: {
		extend: {},
	},
	plugins: [],
};

```

```js
// postcss.config.js
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```
3. Add the Tailwind directives to CSS
```css
/* in src/assets/css/main.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

4. Import Element & tailwind css
```js
// main.js
import { createApp } from "vue";
import "./assets/css/main.css";
import ElementPlus from "element-plus"; // 导入 ElementPlus 组件库的所有模块和功能
import "element-plus/dist/index.css"; // 导入 ElementPlus 组件库所需的全局 CSS 样式
import * as ElementPlusIconsVue from "@element-plus/icons-vue" // 导入 ElementPlus 组件库的所有图标
import App from "./App.vue";

const app = createApp(App);

for (const [key, component] of Object.entries(ElementPlusIconsVue)){
    app.component(key, component)
}

app.use(ElementPlus);
app.mount("#app");

```
5. example of usage (element buttons & icon) with tailwinds css
```html
<template>
	<div class="">
		<div>
			<h3 class="text-xl font-bold underline m-4">Button type</h3>
			<div class="m-4">
				<el-button>Default Button</el-button>
				<el-button type="primary">Primay Button</el-button>
				<el-button type="success">Success Button</el-button>
				<el-button type="info">Info Button</el-button>
				<el-button type="warning">Warning Button</el-button>
				<el-button type="danger">Danger Button</el-button>
			</div>
		</div>
		<div>
			<h3 class="text-xl font-bold underline m-4">Button Attribute</h3>
			<div class="m-4">
				<el-button plain>Plain Default Button</el-button>
				<el-button round type="primary">Round</el-button>
				<el-button circle type="success">C</el-button>
				<el-button disabled type="info">Disabled Info Button</el-button>
				<el-button loading type="warning"
					>Loading Warning Button</el-button
				>
			</div>
		</div>

		<div>
			<h3 class="text-xl font-bold underline m-4">Button Size</h3>
			<div class="m-4">
				<el-button size="large" type="primary">large</el-button>
				<el-button>Default</el-button>
				<el-button size="small" type="warning">Small</el-button>
			</div>
		</div>

		<div>
			<h3 class="text-xl font-bold underline m-4">Icon</h3>
			<div class="m-4">
				<el-icon><Plus /></el-icon>
				<el-icon><Edit /></el-icon>
				<el-icon><Delete /></el-icon>
				<el-icon class="is-loading"><Loading /></el-icon>
			</div>
		</div>

		<div>
			<h3 class="text-xl font-bold underline m-4">Icon Attribute</h3>
			<div class="m-4">
				<el-icon size="30" color="red"><Search /> </el-icon>
				<span> Red 30 Search </span>
			</div>
		</div>

		<div>
			<h3 class="text-xl font-bold underline m-4">Icon Button</h3>
			<div class="m-4">
				<el-button type="primary">
					<el-icon size="20"><Search /> </el-icon>
					<span>Search </span>
				</el-button>
			</div>
		</div>

		<div>
			<h3 class="text-xl font-bold underline m-4">Button Group</h3>
			<div class="m-4">
				<el-button-group>
					<el-button type="primary">
						<el-icon size="20"><Plus /> </el-icon>
					</el-button>
					<el-button type="primary">
						<el-icon size="20"><Edit /> </el-icon>
					</el-button>
					<el-button type="primary">
						<el-icon size="20"><Delete /> </el-icon>
					</el-button>
				</el-button-group>
			</div>
		</div>
	</div>
</template>

<script setup>
</script>

<style lang="scss" scoped></style>

```

### VSCode Extension for tailwind css

#### Tailwind CSS IntelliSense
1. setting in `setting.json` for IntelliSense
```json
"tailwindCSS.includeLanguages": {
    "html": "html",
    "javascript": "javascript",
    "css": "css"
},
"editor.quickSuggestions": {
    "strings": true
},
```

