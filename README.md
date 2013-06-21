aftersave
=========

Sublime Text 2 Plugin which perform a custom action after saving a file



Install
--------

Install it via Package Manager



How it works
-------------

Adding a simple comment at the top of the file in which you want to trigger  a command.

Example:

```
/* aftersave: uglifyjs <self> -o ../public/js/main.js */
(function($){
	$(document).on('ready', function(event) {
		alert('Document is ready!');
	});
})(jQuery);
```


**&lt;self&gt;** is automatically replaced by the current file name.


Known issues
-------------------

It probably won't work in Windows.
