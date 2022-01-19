<template>
    <nav class="navbar navbar-expand-lg nav">
    <div class="container-fluid">
    <a class="navbar-brand link" href="#">AppAdmin</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav list">
        <li class="nav-item">
            <router-link to="/" class="nav-link link" aria-current="page"><strong>Home</strong></router-link>
        </li>
        <li class="nav-item">
            <router-link to="/Ingresos" class="nav-link link" aria-current="page"><strong>Ingresos</strong></router-link>
        </li>
        <li class="nav-item">
            <router-link to="/Gastos" class="nav-link link" aria-current="page"><strong>Gastos</strong></router-link>
        </li>
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle link" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            <strong>Codigos</strong>
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
            <li><router-link to="/Code/Bank" class="dropdown-item" aria-current="page"><strong>Bancos</strong></router-link></li>
            <li><router-link to="/Code/Income" class="dropdown-item" aria-current="page"><strong>Ingresos</strong></router-link></li>
            <li><router-link to="/Code/Spend" class="dropdown-item" aria-current="page"><strong>Gastos</strong></router-link></li>
        </ul>
        </li>
    </ul>
    </div>

</div>
</nav>
</template>
<script>
export default {
	name: 'Navbar'
}
</script>
