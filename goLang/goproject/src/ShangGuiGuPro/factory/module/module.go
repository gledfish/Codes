package module

type student struct {
	Name string
	score float64
}
func (stu *student) GetScore () float64 {
	return stu.score
}