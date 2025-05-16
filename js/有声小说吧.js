var rule = {
    title: '有声小说吧',
    编码: 'gb18030',
    host: 'http://m.ysxs8.top',
    url: '/downlist/fyclass_fypage.html',
    searchUrl: '/search.asp?page=fypage&searchword=**&searchtype=-1',
    searchable: 2,
    quickSearch: 0,
    headers: {
        'User-Agent': 'MOBILE_UA'
    },
    timeout: 5000,
    class_name: '网络玄幻&恐怖悬疑&传统武侠&都市言情&官场刑侦&历史军事&探险盗墓&职场商战&明朝那些事儿&评书下载&相声戏曲&人物传记&广播剧&百家讲坛&外语读物&有声文学&儿童读物&管理营销',
    class_url: 'r52&r17&r12&r13&r14&r15&r45&r81&r36&r3&r7&r16&r18&r32&r35&r41&r4&r6',
    play_parse: true,
    lazy: '',
    limit: 6,
    推荐: '.list-ul .list-li;.list-name&&Text;*;.module-slide-author&&Text;*',
    一级: '.book-ol&&li;h4&&Text;img&&data-original;.book-meta&&Text;a&&href',
    二级: {
        title: 'h1&&Text',
        img: '.book img&&src',
        desc: '.book-des p&&Text',
        content: '.book-des--p&&Text',
        tabs: '.playlist-top&&h2',
        lists: '#playlist ul li',
        playerTitle: '.fonhen-player-title&&Text', // 新增字段，提取播放器标题
        playerTime: '.jp-current-time&&Text', // 新增字段，提取当前播放时间
        playerDuration: '.jp-duration&&Text', // 新增字段，提取总时长
        playerProgress: 'js:let progressBar=document.querySelector(".jp-play-bar");progressBar.style.width', // 新增字段，提取播放进度百分比
    },
    搜索: '*',
}
