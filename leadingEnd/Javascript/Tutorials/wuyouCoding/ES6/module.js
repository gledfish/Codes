// 导出方式
export const aTitle = 'a模块的标题'
export function aFn(){
    console.log("a模块的方法")
}

export default {// 默认导出
    name:"模块" 
}

// 统一导出方式
module.exports = {
    
}
// 导入方法
// import moduleName from path 