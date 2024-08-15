<script>
	import { BlogStore } from './../../BlogStore';

	onMount(async function () {
		if ($BlogStore.length) {
            const endpoint = 'http://127.0.0.1:8000/api/blogs/';
			const response = await fetch(endpoint);
			const data = await response.json();

			console.log(data)

			BlogStore.set(data);
		}
	});
</script>

<div class="max-w-3xl mx-auto p-4 bg-white shadow rounded-lg">
	{#each $BlogStore as blog}
		<div class="my-4 p-5 border-b last:border-b-0">
			<h1 class="text-2xl font-bold text-gray-900">{blog.title}</h1>
			<p class="text-gray-600">{blog.description}</p>
			<p class="text-sm text-gray-400">{blog.created_at}</p>
		</div>
	{/each}
</div>
