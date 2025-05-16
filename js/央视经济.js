var rule = {
    title:'央视频',
    host:'https://api.cntv.cn',
    homeUrl: '/lanmu/columnSearch?&fl=&fc=&cid=&p=1&n=500&serviceId=tvcctv&t=json',
  //  url:'/list/getVideoAlbumList?fyfilter&area=&letter=&n=24&serviceId=tvcctv&t=json',
  url: '/NewVideo/getVideoListByColumn?id=fyclass&n=10&sort=desc&p=fypage&mode=0&serviceId=tvcctv',
    searchUrl:'',
    searchable:0,
    quickSearch:0,
    
  class_name: '对话&经济半小时&经济信息联播&第一时间&消费主张&欢乐大猜想&创业英雄汇&生财有道&职场健康课&一锤定音&回家吃饭&央视财经评论&中国经济大讲堂&正点财经&天下财经&生活家&魅力中国城',
  class_url: 'TOPC1451530382483536&TOPC1451533652476962&TOPC1451533782742171&TOPC1451530259915198&TOPC1451534775834896&TOPC1672292475106944&TOPC1451529684665516&TOPC1451534118159896&TOPC1467078494968390&TOPC1451538759798817&TOPC1451532939300997&TOPC1451538686034772&TOPC1514182710380601&TOPC1453100395512779&TOPC1451531385787654&TOPC1593419181674791&TOPC1499160712571517',

    filterable: 1,  
    headers:{
        'User-Agent':'PC_UA'
    },
    timeout:10000,
    play_parse:true,
    
    limit:6,
    double:false,
/*
    推荐: $js.toString(() => {
        var d = [];
        var list = JSON.parse(request(input)).response.docs;

        list.forEach(it => {
            // 一级标题
            let title1 = it.column_name;
            // 一级描述
            let desc1 = it.channel_name;
            // 一级图片URL
            let picUrl1 = it.column_logo;
            // 一级URL（id 地区 类型 标题 演员 年份 频道 简介 图片 更新至）
            let url1 = it.lastVIDE.videoSharedCode + '|' + '' + '|' + it.column_firstclass + '|' + it.column_name + '|' + '' + '|' + it.column_playdate + '|' + it.channel_name + '|' + it.column_brief + '|' + it.column_logo + '|' + '' + '|' + it.lastVIDE.videoTitle;

            d.push({
                desc : desc1,
                title : title1,
                pic_url : picUrl1,
                url : url1
            })
        })
        setResult(d);
    }),
*/
    
    一级: $js.toString(() => {

        var d = [];

           var list = JSON.parse(request(input)).data.list;
            list.forEach(it => {
            //一级id           
                let guid1 = it.guid;
                // 一级标题
                let title1 = it.title
                // 一级描述
                let desc1 = it.time;
                // 一级图片URL
                let picUrl1 = it.image;
                // 一级URL（id 地区 类型 标题 演员 年份 频道 简介 图片 集数）
             let url1 =it.guid + '|' + it.id + '|' + it.time + '|' + it.title + '|' + it.length + '|' + it.image + '|' + it.focus_date + '|' + it.brief  + '|' + it.url + '|'   + '' + '|' + MY_CATE;
                d.push({
                    desc : desc1,
                    title : title1,
                    pic_url : picUrl1,
                    guid : guid1,
                    url : url1
                })
            })
        setResult(d);
    }),

二级 : $js.toString(() => {
let info = input.split("|");
let guid = info[0].replaceAll('https://api.cntv.cn/lanmu/', '');
    VOD = {
            vod_id: info[1],
            vod_name: info[3],
            vod_pic: info[5],
            type_name: info[2],
            vod_year: info[2],
            vod_area: info[1],
            vod_remarks: '🐉龙少爷🐉龙少爷',
            vod_director: '🐉龙少爷🐉龙少爷',
            vod_actor: '🐉龙少爷🐉龙少爷',
            vod_content: info[7],
        vod_play_from: '央视频',
        vod_play_url: '立即播放$https://hls.cntv.myhwcdn.cn/asp/hls/850/0303000a/3/default/' + guid + '/850.m3u8'
    };

}),
    搜索:'',
}