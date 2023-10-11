package monster

import (
	"testing"
)

func TestStore(t *testing.T) {
	//创建一个monster实例
	monster := &Monster {
		Name : "红孩儿",
		Age : 10,
		Skill : "三味真火",
	}
	res := monster.Store()
	if !res {
		t.Fatalf("expected %v, result is %v", true, res)
	}
	t.Logf("Testing succeed!")
}

func TestReStore(t *testing.T) {
	//创建一个monster实例
	monster := &Monster {}
	res := monster.ReStore()
	if !res {
		t.Fatalf("expected %v, result is %v", true, res)
	}
	t.Logf("Testing succeed!")
}