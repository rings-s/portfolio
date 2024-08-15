<script>
    import { ClientStore } from './../../ClientStore';

    onMount(async function () {
        if ($ClientStore.length) {
            const endpoint = `http://127.0.0.1:8000/api/clients/`
            const response = await fetch(endpoint)
            const data = await response.json()

            // console.log(data)

            ClientStore.set(data)

        }
       
    })
</script>

<div class="max-w-4xl mx-auto p-4 bg-white shadow rounded-lg">
    {#each $ClientStore as client}
        <div class="my-4 p-5 border-b last:border-b-0">
            <h1 class="text-2xl font-bold text-gray-900">{client.name}</h1>
            <p class="text-gray-600">{client.phone_number}</p>
            <p class="text-sm text-gray-400">{client.created_at}</p>
        </div>
    {/each}

 
</div>
