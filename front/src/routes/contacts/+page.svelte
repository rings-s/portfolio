<script>
    import { ContactStore } from './../../ContactStore';

    let handleClick = () => ContactStore.update(prev => {
        let newContact = { id: 3, name: 'Drive', email: '123456789', message: 'Nicolas Winding Refn', created_at: '2022-01-01' };
        return [...prev, newContact];
    });
</script>

<div class="max-w-4xl mx-auto p-4 bg-white shadow-lg rounded-lg">
    {#each $ContactStore as contact}
        <div class="p-4 mb-4 border-b last:border-b-0 rounded">
            <h1 class="text-xl font-semibold text-gray-900">{contact.name}</h1>
            <p class="text-gray-600">{contact.email}</p>
            <p class="text-sm text-gray-500">{contact.message}</p>
        </div>
    {/each}

    <button type="button" class="px-4 py-2 mt-4 bg-blue-600 hover:bg-blue-700 text-white font-bold rounded-md transition-colors" on:click={handleClick}>
        Add a Contact
    </button>
</div>
