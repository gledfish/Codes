
// 使用String、Integer等类型的时候，这些类型都是不变类，一个不变类具有以下特点：

// 定义class时使用final，无法派生子类；
// 每个字段使用final，保证创建实例后无法修改任何字段。
// public final class Point {
//     private final int x;
//     private final int y;

//     public Point(int x, int y) {
//         this.x = x;
//         this.y = y;
//     }

//     public int x() {
//         return this.x;
//     }

//     public int y() {
//         return this.y;
//     }
// }

//使用record
public record Point(int x, int y) {
    }