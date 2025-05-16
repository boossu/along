var rule = {
    title:'央视频',
    host:'https://api.cntv.cn',
    homeUrl: '/lanmu/columnSearch?&fl=&fc=&cid=&p=1&n=500&serviceId=tvcctv&t=json',
  //  url:'/list/getVideoAlbumList?fyfilter&area=&letter=&n=24&serviceId=tvcctv&t=json',
  url: '/NewVideo/getVideoListByColumn?id=fyclass&n=10&sort=desc&p=fypage&mode=0&serviceId=tvcctv',
    searchUrl:'',
    searchable:0,
    quickSearch:0,
    class_name: '焦点访谈&每周质量报告&午夜新闻&新闻调查&新闻周刊&面对面&法治在线&新闻30分&新闻1+1&军情时间到&国际时讯&新闻直播间&朝闻天下&世界周刊&高端访谈&环球视线&共同关注&24小时&东方时空',
class_url:'TOPC1451558976694518&TOPC1451558650605123&TOPC1451558779639282&TOPC1451558819463311&TOPC1451559180488841&TOPC1451559038345600&TOPC1451558590627940&TOPC1451559097947700&TOPC1451559066181661&TOPC1462504102545692&TOPC1451558887804404&TOPC1451559129520755&TOPC1451558496100826&TOPC1451558687534149&TOPC1665739007799851&TOPC1451558926200436&TOPC1451558858788377&TOPC1451558428005729&TOPC1451558532019883',  
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