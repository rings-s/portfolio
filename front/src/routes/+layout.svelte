<script>
    import '../app.postcss';
    import { AppShell, AppBar } from '@skeletonlabs/skeleton';

    // Floating UI for Popups
    import { computePosition, autoUpdate, flip, shift, offset, arrow } from '@floating-ui/dom';
    import { storePopup } from '@skeletonlabs/skeleton';
    storePopup.set({ computePosition, autoUpdate, flip, shift, offset, arrow });

    let isOpen = false;

    // Function to toggle the menu state
    const toggleMenu = () => {
        isOpen = !isOpen;
    };
</script>

<div>
    <header class="bg-white shadow-md">
        <div class="max-w-7xl bg-white mx-auto px-4 sm:px-6 lg:px-8 flex flex-col lg:flex lg:flex-row  justify-between lg:items-center relative">
            <h1 class="text-lg leading-6 font-semibold text-black my-4 lg:order-1">
                <a href="/" class="hover:text-gray-700 transition duration-150 ease-in-out">Ringo</a>
            </h1>

            <nav aria-label="Main navigation" class=" lg:order-2 w-full lg:w-auto">
                <!-- Toggle button, hidden on large screens -->
                <button 
                    class="absolute  right-0 top-2 p-2 border-none cursor-pointer text-black lg:hidden" 
                    on:click={toggleMenu} 
                    aria-label="Toggle navigation"
                >
                    <!-- Toggle button icon changes based on the state -->
                    {#if isOpen}
                        <svg viewBox="0 0 24 24" width="24" height="24">
                            <path d="M6 18L18 6M6 6l12 12" fill="none" stroke="black" stroke-width="2" /> <!-- Close Icon -->
                        </svg>
                    {:else}
                        <svg viewBox="0 0 24 24" width="24" height="24">
                            <path d="M3 6h18M3 12h18m-18 6h18" fill="none" stroke="black" stroke-width="2" /> <!-- Hamburger Icon -->
                        </svg>
                    {/if}
                </button>

                <!-- Navigation links, toggled on small screens and always visible on large screens -->
                <ul class={`lg:flex items-center justify-center gap-4 ${isOpen ? 'flex flex-col items-center w-full' : 'hidden'} lg:flex`}>
                    <li><a href="/" class="text-base text-black hover:text-gray-900">Home</a></li>
                    <li><a href="/about" class="text-base text-black hover:text-gray-900">About</a></li>
                    <li><a href="/services" class="text-base text-black hover:text-gray-900">Services</a></li>
                    <li><a href="/projects" class="text-base text-black hover:text-gray-900">Projects</a></li>
                    <li><a href="/testimonials" class="text-base text-black hover:text-gray-900">Testimonials</a></li>
                    <li><a href="/contacts" class="text-base text-black hover:text-gray-900">Contacts</a></li>
                    <li><a href="/blogs" class="text-base text-black hover:text-gray-900">Blogs</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <slot />
</div>

