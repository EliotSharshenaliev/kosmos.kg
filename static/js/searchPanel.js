let $topeContainer = $('.isotope-grid');


function filterItems(event) {
    let searchTerm = event.target.value.toLowerCase()
    $topeContainer.isotope({
        filter: function() {
            let itemText = $(this).attr("data-filter").toLowerCase();
            let filter = $('.how-active1').attr("data-filter").replace(".", "")
            if (filter !== "*"){
                return itemText.indexOf(searchTerm) > -1 && this.classList.contains(filter)
            }
            return itemText.indexOf(searchTerm) > -1
        }
    });
}
$('.search-panel-input').on('input', filterItems);


