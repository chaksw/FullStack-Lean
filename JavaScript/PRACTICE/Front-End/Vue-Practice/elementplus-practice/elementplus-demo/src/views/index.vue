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
