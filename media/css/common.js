var $wg = function (id) {
    return document.getElementById(id)
};
var viewcss = ['open', 'close'],
    showsearch = 0,
    showmenu = 0,
    nPosition;
var firstPic = true,
    wpArr = [],
    wpNum = 0,
    csPic = 0,
    litime, limsta = 0,
    limcur = 0;
var ascroll, dvalue, bscroll = scrolltopnow(),
    scrollbtn = $wg('topbtn');
//顶部导航
function opensearch() {
    $wg('search').className = 'search ' + viewcss[showsearch];
    (showsearch == 1) ? showsearch = 0: showsearch = 1;
}
//执行搜索
function gosearch() {
    var keytext = $wg('searchtext').value;
    if (keytext != '') {
        document.forms.submit();
    }
}
//返回顶部
function scrolltopnow() {
    return document.documentElement.scrollTop || document.body.scrollTop;
}

function goscrolltop() {
    if (document.documentElement.scrollTop) {
        document.documentElement.scrollTop = 0;
    } else {
        document.body.scrollTop = 0;
    }
}
//图片延迟加载
function findPics() {
    var picList = $wg('piclist').getElementsByTagName('img');
    var pn = picList.length;
    var p = 0;
    for (var i = 0; i < pn; i++) {
        if (picList[i].className != 'loaded') {
            wpArr[p] = picList[i];
            p++;
        }
    }
    wpNum = p;
    csPic = p;
}

function givemepic() {
    var isltop = document.documentElement.scrollTop || document.body.scrollTop;
    var iclheight = document.documentElement.clientHeight + isltop + 300;
    var iTop = 0,
        iBottom = 0,
        oParent = null;
    for (var u = 0; u < wpNum; u++) {
        if (wpArr[u] != null) {
            oParent = wpArr[u].parentElement || wpArr[u].parentNode;
            iTop = wpArr[u].offsetTop;
            iBottom = iTop + oParent.offsetHeight;
            if (iTop > isltop && iTop < iclheight || (iBottom > isltop && iBottom < iclheight)) {
                wpArr[u].src = wpArr[u].getAttribute('data-img');
                wpArr[u].className = 'loaded';
                wpArr[u] = null;
                csPic--;
                break;
            }
        }
    }
}

function piclimit() {
    if (firstPic) {
        findPics();
        firstPic = false;
    }
    if (csPic > 0) {
        clearTimeout(litime);
        limcur = new Date();
        if (limsta == 0) {
            limsta = limcur;
        }
        if (limcur - limsta > 500) {
            givemepic();
            limsta = limcur;
        } else {
            litime = setTimeout(givemepic, 250);
        }
    }
}
//统计
function sendwData() {
    console.log('sendwData do nothing!');
}
//window.addEventListener('scroll', piclimit, false);
window.onscroll = function () {
    ascroll = scrolltopnow();
    dvalue = ascroll - bscroll;
    if (dvalue > 0) {
        scrollbtn.style.display = 'none';
    } else {
        if (ascroll > 300) {
            scrollbtn.style.display = 'block';
        } else {
            scrollbtn.style.display = 'none';
        }
    }
    bscroll = ascroll;
};
sendwData();