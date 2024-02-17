document.getElementById('check_all').onclick = function() {
    var checkboxes = document.getElementsByName('row_check');
    for (var checkbox of checkboxes) {
        checkbox.checked = this.checked;
    }
}