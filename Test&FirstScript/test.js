(function () {
    var link;
    link = mw.util.addPortletLink('p-tb', '#', 'מעקב למידה');

    if (!link) {
        return;
    }

    link.onclick = function (event) {

        event.preventDefault();

        var title = $('.firstHeading').text();
        var isCategory = title.includes('קטגוריה:');

        if (isCategory) {
            $('.firstHeading').append('<p>[ (%xx) 1/n ]</p>');
            /*var pages = $('.mw-category');
        	var c = pages.children();
        	for(var i = 0 ; i<c.length ; i++)
        	{
        		sub = c[i].childNodes;
        		console.log(sub[1].tagName);
        	}*/
            $('#mw-subcategories').find('div').find('ul').find('li').append('<p>[ 1/m ]</p>');
        }
        else {
            $('.mw-parser-output')
    		.prepend('<label id="label-done"><input id="checkBox" name="done" value="myValue" type="checkbox">בוצע </label>');
        }

        $(document).ready(function () {
            $("#checkBox").click(function () {
                var done = "done";
                if ($("#checkBox").is(':checked')) {
                    //alert("Checked");
                    console.log("Checked!");
                }
                else {
                    //alert("unChecked");
                    console.log("unChecked!");
                }
            });
        });

        $('.mw-list-item-js').children('a').click(function () {
            return false;
        });
    };

}())