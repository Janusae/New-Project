jQuery(document).ready(function(event) {
	var animating = false,
		firstLoad = false;
	$('main').on('click', '[data-type="page-transition"]', function(event) {
		event.preventDefault();
		var newPage = $(this).attr('href');
		if (!animating)
			changePage(newPage, true);
		firstLoad = true;
	});
	$(window).on('popstate', function() {
		if (firstLoad) {
			var newPageArray = location.pathname.split('/'),
				newPage = newPageArray[newPageArray.length - 1];
			if (!animating)
				changePage(newPage, false);
		}
		firstLoad = true;
	});
	function changePage(url, bool) {
		animating = true;
		$('body').addClass('page-is-changing');
		$('.cd-loading-bar').one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend', function() {
			loadNewContent(url, bool);
			$('.cd-loading-bar').off('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend');
		});
		if (!transitionsSupported())
			loadNewContent(url, bool);
	}
	function loadNewContent(url, bool) {
		url = ('' == url) ? 'index.html' : url;
		var newSection = 'cd-' + url.replace('.html', '');
		var section = $('<div class="cd-main-content ' + newSection + '"></div>');
		section.load(url + ' .cd-main-content > *', function(event) {
			$('main').html(section);
			var delay = (transitionsSupported()) ? 1200 : 0;
			setTimeout(function() {
				(section.hasClass('cd-about')) ? $('body').addClass('cd-about') : $('body').removeClass('cd-about');
				$('body').removeClass('page-is-changing');
				$('.cd-loading-bar').one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend', function() {
					animating = false;
					$('.cd-loading-bar').off('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend');
				});
				if (!transitionsSupported())
					animating = false;
			}, delay);
			if (url != window.location && bool) {
				window.history.pushState({
					path: url
				}, '', url);
			}
		});
	}
	function transitionsSupported() {
		return $('html').hasClass('csstransitions');
	}
});

