function formatarMoeda(campo) {
    campo.addEventListener('input', function(e) {
        let valor = e.target.value.replace(/\D/g, '');
        valor = (valor / 100).toFixed(2) + '';
        valor = valor.replace('.', ',');
        valor = valor.replace(/\B(?=(\d{3})+(?!\d))/g, '.');
        e.target.value = valor;
    });
}

window.onload = function() {
    formatarMoeda(document.getElementById('salario'));
    formatarMoeda(document.getElementById('valor'));
    formatarMoeda(document.getElementById('entrada'));
};