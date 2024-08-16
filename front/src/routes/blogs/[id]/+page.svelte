<script>
	import { BlogStore } from '../../../BlogStore';
	import { onMount } from 'svelte';

	onMount(async () => {
		try {
			const endpoint = 'http://127.0.0.1:8000/api/blogs/';
			const response = await fetch(endpoint);
			if (!response.ok) {
				throw new Error(`HTTP error! status: ${response.status}`);
			}
			const data = await response.json();
			console.log(data);
			BlogStore.set(data);
		} catch (error) {
			console.error('Failed to fetch blogs:', error);
		}
	});
</script>

	<div class=" mt-12">
		<div class="max-w-3xl mx-auto p-4 bg-white shadow rounded-lg ">
			{#each $BlogStore as blog}
				<div class="my-4 p-5 border-b last:border-b-0">
					<h1 class="text-2xl font-bold text-gray-900">{blog.title}</h1>
					<p class="text-sm text-gray-800">{blog.description}</p>
				</div>
				<a href="/blogs/" class="text-gray-600">blogs</a>

			{/each}
		</div>


	</div>

