(function () {

    var link, ls, pt;
    var i = 0;
    link = mw.util.addPortletLink('p-tb', '#', '���� �����');

    if (!link) {
        return;
    }
    link.onclick = function (event) {

        event.preventDefault();


        function recalculate() {

            alert('��� ������ �� ��� ����� ������ ���?');

            pt = mw.util.addPortletLink('p-tb', '#', "WikiPage::getId()");

            localStorage.setItem("lastname", "john1");
            document.getElementById("btn").innerHTML = localStorage.getItem("lastname");

        }

        mw.util.$content.find(".firstHeading").after(
            $('<div>', { 'id': 'btn', 'class': 'voteCounterSpan' })
                .css({ 'font-size': '140%', 'margin-bottom': '20px', padding: '8px', width: 'auto' })
                .text('����')
                .append(
                    $('<input>', { 'type': 'checkbox' })
                    .change(recalculate)
                    )
                .append($('<span>', { 'class': 'voteResults' }))
      );
    };

}());
if (localStorage.lastname) {
    pt = mw.util.addPortletLink('p-tb', '#', "�����?? ��� ����� ���");
    alert('����� �����??');

}