var rule = {
    title:'央视频',
    host:'https://api.cntv.cn',
    homeUrl: '/lanmu/columnSearch?&fl=&fc=&cid=&p=1&n=500&serviceId=tvcctv&t=json',
  //  url:'/list/getVideoAlbumList?fyfilter&area=&letter=&n=24&serviceId=tvcctv&t=json',
  url: '/NewVideo/getVideoListByColumn?id=fyclass&n=10&sort=desc&p=fypage&mode=0&serviceId=tvcctv',
    searchUrl:'',
    searchable:0,
    quickSearch:0,
    
class_name: '动画大放映&第一动画乐园&健康之路&走进科学&探索·发现&动物世界&人与自然&自然传奇&地理·中国&远方的家&跟着书本去旅行&百家讲坛&空中剧院&体坛快讯&新闻联播&焦点访谈&今日说法&等着我&新闻直播间&海峡两岸&天网&今日关注&高端访谈&开讲啦&故事里的中国&对话&面对面&是真的吗&星光大道&精彩音乐汇&音乐厅&民歌·中国&中国电影报道&星推荐&方圆剧阵&正大综艺&第一时间&开门大吉&开讲啦&共同关注&军事报道&新闻调查&新闻 30 分&新闻 1+1&今日亚洲&新闻直播间&24 小时&中国新闻&午夜新闻&朝闻天下&晚间新闻&新闻周刊&经济半小时&经济大讲堂&正点财经&生活圈&生活提示&东方时空&经济信息联播&今日环球&一线',
class_url:'TOPC1451559025546574&TOPC1451378857272262&TOPC1451557646802924&TOPC1451558190239536&TOPC1451557893544236&TOPC1451378967257534&TOPC1451525103989666&TOPC1451558150787467&TOPC1451557421544786&TOPC1451541349400938&TOPC1575253587571324&TOPC1451557052519584&TOPC1451558856402351&TOPC1451550970356385&TOPC1451528971114112&TOPC1451558976694518&TOPC1451464665008914&TOPC1451378757637200&TOPC1451559129520755&TOPC1451540328102649&TOPC1451530382483536&TOPC1451540389082713&TOPC1665739007799851&TOPC1451464884159276&TOPC1451464884159276&TOPC1514182710380601&TOPC1451559038345600&TOPC1451534366388377&TOPC1451467630488780&TOPC1451541414450906&TOPC1451534421925242&TOPC1451541994820527&TOPC1451354597100320&TOPC1451469943519994&TOPC1571217727564820&TOPC1650782829200997&TOPC1451530259915198&TOPC1451465894294259&TOPC1451464884159276&TOPC1451558858788377&TOPC1451527941788652&TOPC1451558819463311&TOPC1451559097947700&TOPC1451559066181661&TOPC1451540448405749&TOPC1451559129520755&TOPC1451558428005729&TOPC1451539894330405&TOPC1451558779639282&TOPC1451558496100826&TOPC1451528792881669&TOPC1451559180488841&TOPC1601362002656197&TOPC1451533652476962&TOPC1453100395512779&TOPC1451546588784893&TOPC1451526037568184&TOPC1451558532019883&TOPC1451533782742171&TOPC1571034705435323&TOPC1451543462858283',


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