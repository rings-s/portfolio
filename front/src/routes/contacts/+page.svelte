<script>
import { ContactStore } from '../../ContactStore';
import { goto } from '$app/navigation';
    let name = '';
    let email = '';
    let message = '';
    let showInvalidMessage = false;

    let validFields = () => {
        return name.length > 4 && email.includes('@') && message.length > 10;
    }

    let handleSubmit = () => {
        if (!validFields()) {
            showInvalidMessage = true;
            return;
        }

        const endpoint = 'http://localhost:8000/api/contacts/';
        let data = new FormData();
        data.append('name', name);
        data.append('email', email);
        data.append('message', message);
        fetch(endpoint, {method: 'POST', body: data}).then(response => response.json()).then(data => {
            ContactStore.update(prev => [...prev, data]);
        });

        // redirect after submit using goto
        goto('/projects/');
    }
</script>
<div class="text-center mt-12 px-4 sm:px-6 lg:px-8">
    {#if showInvalidMessage}
        <p class="text-red-500">Please fill all the fields correctly.</p>
    {/if}

    <form class="space-y-6 w-full max-w-lg mx-auto" on:submit|preventDefault={handleSubmit}>
        <div>
            <input type="text" class="form-input w-full text-black border border-gray-300 rounded-lg p-4 focus:ring-2 focus:ring-blue-500 focus:outline-none transition duration-150 ease-in-out" placeholder="Name" bind:value={name} />
        </div>

        <div>
            <input type="email" class="form-input w-full text-black border border-gray-300 rounded-lg p-4 focus:ring-2 focus:ring-blue-500 focus:outline-none transition duration-150 ease-in-out" placeholder="Email" bind:value={email} />
        </div>

        <div>
            <textarea class="form-input w-full text-black border border-gray-300 rounded-lg p-4 focus:ring-2 focus:ring-blue-500 focus:outline-none transition duration-150 ease-in-out" placeholder="Message" bind:value={message} rows="4"></textarea>
        </div>

        <button class="w-full mt-4 px-6 py-3 bg-gray-700 hover:bg-gray-800 text-white font-semibold border border-gray-100 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-700 focus:ring-opacity-50 transition duration-150 ease-in-out">Submit</button>
    </form>
</div>
