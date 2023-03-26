// 获取导航栏元素
const navbar = document.querySelector('.navbar');
// 获取导航栏切换按钮
const navbarToggler = document.querySelector('.navbar-toggler');
// 获取顶部图像元素
const heroImg = document.querySelector('.hero-img');
// 获取下拉箭头元素
const arrow = document.querySelector('.arrow');

// 导航栏切换
navbarToggler.addEventListener('click', () => {
    navbar.classList.toggle('active');
});

// 顶部图像缩放
heroImg.addEventListener('mouseenter', () => {
    heroImg.style.transform = 'scale(1.1)';
});

heroImg.addEventListener('mouseleave', () => {
    heroImg.style.transform = 'scale(1)';
});

// 下拉箭头动画
arrow.addEventListener('click', () => {
    window.scrollTo({
        top: window.innerHeight,
        behavior: 'smooth',
    });
});
