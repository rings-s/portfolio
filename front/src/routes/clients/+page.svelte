<script>
    import { ClientStore } from './../../ClientStore';

    let handleClick = () => ClientStore.update(prev => {
        let newClient = { id: 3, name: 'Drive', phone_number: '123456789', created_at: '2022-01-01' };
        return [...prev, newClient];
    });
</script>

<div class="max-w-4xl mx-auto p-4 bg-white shadow rounded-lg">
    {#each $ClientStore as client}
        <div class="my-4 p-5 border-b last:border-b-0">
            <h1 class="text-2xl font-bold text-gray-900">{client.name}</h1>
            <p class="text-gray-600">{client.phone_number}</p>
            <p class="text-sm text-gray-400">{client.created_at}</p>
        </div>
    {/each}

    <button type="button" class="px-4 py-2 mt-3 bg-blue-500 hover:bg-blue-600 text-white font-semibold rounded-md shadow" on:click={handleClick}>
        Add a Client
    </button>
</div>
