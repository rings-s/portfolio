<script>
    import { TestimonialStore } from './../../TestimonialStore';

    onMount(async function () {
        if ($TestimonialStore.length) {
            const endpoint = 'http://127.0.0.1:8000/api/testimonials/'
            const response = await fetch(endpoint)
            const data = await response.json()

            // console.log(data)

            TestimonialStore.set(data)

        }
       
    })
</script>

<div class="max-w-6xl mx-auto p-5">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {#each $TestimonialStore as testimonial}
            <div class="bg-white shadow-lg rounded-lg p-6 flex flex-col justify-between">
                <div>
                    <h1 class="text-xl font-bold text-gray-900">{testimonial.client_name}</h1>
                    <p class="text-gray-700">{testimonial.project_name}</p>
                    <p class="text-sm text-gray-500">{testimonial.date}</p>
                    <p class="text-gray-600 mt-2">{testimonial.testimonial_body}</p>
                </div>
            </div>
        {/each}
    </div>

</div>
