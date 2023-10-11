package main

import "testing"

func TestAddUpper(t *testing.T) {
	if ans := addUpper(10); ans != 55 {
		t.Errorf("expected ans = %d, but result = %d", 55, ans)
	}
}