document.addEventListener('DOMContentLoaded', function () {
    // Get the dropdown button and menu
    const dropdownToggle = document.getElementById('profileDropdown');
    const dropdownMenu = document.querySelector('.dropdown-menu');

    // Toggle dropdown menu visibility on button click
    dropdownToggle.addEventListener('click', function (event) {
        event.stopPropagation(); // Prevent click event from bubbling up
        dropdownMenu.classList.toggle('show');
    });

    // Close dropdown if clicking outside of it
    document.addEventListener('click', function () {
        if (dropdownMenu.classList.contains('show')) {
            dropdownMenu.classList.remove('show');
        }
    });
});

// smooth scroll
$(document).ready(function(){
    $(".navbar .nav-link").on('click', function(event) {

        if (this.hash !== "") {

            event.preventDefault();

            var hash = this.hash;

            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 700, function(){
                window.location.hash = hash;
            });
        }
    });
});

// protfolio filters
$(window).on("load", function() {
    var t = $(".portfolio-container");
    t.isotope({
        filter: ".new",
        animationOptions: {
            duration: 750,
            easing: "linear",
            queue: !1
        }
    }), $(".filters a").click(function() {
        $(".filters .active").removeClass("active"), $(this).addClass("active");
        var i = $(this).attr("data-filter");
        return t.isotope({
            filter: i,
            animationOptions: {
                duration: 750,
                easing: "linear",
                queue: !1
            }
        }), !1
    })
})

document.addEventListener('DOMContentLoaded', function () {
    // Enable Bootstrap's alert dismissal functionality
    var alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
        var closeButton = alert.querySelector('.close');
        if (closeButton) {
            closeButton.addEventListener('click', function () {
                alert.classList.remove('show');
                alert.classList.add('fade');
            });
        }
    });
});

