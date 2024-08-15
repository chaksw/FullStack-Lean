// 绮樻€у鑸�
const headerEL = document.querySelector("header");
const scrollToTop = document.querySelector(".scrollToTop")
window.addEventListener("scroll", () => {
  let height = headerEL.getBoundingClientRect().height;
  if (window.pageYOffset - height > 800) {
    if (!headerEL.classList.contains("sticky")) {
      headerEL.classList.add("sticky");
    }
  } else {
    headerEL.classList.remove("sticky")
  }
  // 杩斿洖椤堕儴
  if (window.pageYOffset > 2000) {
    scrollToTop.style.display = "block"
  } else {
    scrollToTop.style.display = "none"
  }
})

// 鍒濆鍖栬疆鎾浘
const glide = new Glide(".glide");
const captionsEL = document.querySelectorAll(".slide-caption");


glide.on(["mount.after", "run.after"], () => {
  const caption = captionsEL[glide.index];
  anime({
    targets: caption.children,
    opacity: [0, 1],
    duration: 400,
    easing: 'spring(1, 80, 10, 0)',
    delay: anime.stagger(400, { start: 300 }),
    translateY: [anime.stagger([40, 10]), 0]
  });
});
glide.on("run.before", () => {
  document.querySelectorAll(".slide-caption > *").forEach(el => {
    el.style.opacity = 0;
  });
});
glide.mount();

const isotope = new Isotope(".cases", {
  layoutMode: "fitRows",
  itemSelector: ".case-item"
})
const filterBtns = document.querySelector(".filter-btns");
filterBtns.addEventListener("click", e => {
  let { target } = e;
  const filterOption = target.getAttribute("data-filter");
  if (filterOption) {
    document
      .querySelectorAll(".filter-btn.active")
      .forEach(btn => btn.classList.remove("active"));
    target.classList.add("active");
    isotope.arrange({ filter: filterOption });
  }
})

// 婊戝姩鍑虹幇鍔ㄧ敾
const staggeringOption = {
  delay: 300,
  distance: "50px",
  duration: 500,
  easing: "ease-in-out",
  origin: "bottom"
};
ScrollReveal().reveal(".feature", { ...staggeringOption, interval: 350 })
ScrollReveal().reveal(".service-item", { ...staggeringOption, interval: 350 })

const dataSectionEl = document.querySelector(".data-section");
ScrollReveal().reveal(".data-section", {
  beforeReveal: () => {
    anime({
      targets: ".data-price .num",
      innerHTML: el => {
        return [0, el.innerHTML];
      },
      duration: 2000,
      round: 1,
      easing: "easeInExpo"
    });
    dataSectionEl.style.backgroundPosition =
      `center calc(50% - ${dataSectionEl.getBoundingClientRect().bottom / 5}px)`;
  }
});

// 鏁版嵁鍖哄煙鑳屾櫙鍙樺寲
window.addEventListener("scroll", () => {
  const bottom = dataSectionEl.getBoundingClientRect().bottom;
  const top = dataSectionEl.getBoundingClientRect().top;
  if (bottom > 0 && top < window.innerHeight) {
    dataSectionEl.style.backgroundPosition = `center calc(50%-${bottom / 5}px)`;
  }
});

// 骞虫粦婊氬姩
const scroll = new SmoothScroll('nav a[href*="#"],.scrollToTop a[href*="#"]', {
  header: "header",
  offset: 80
});
//鍏抽棴鍏ㄥ睆瀵艰埅
document.addEventListener("scrollStart", () => {
  if (headerEL.classList.contains("open")) {
    headerEL.classList.remove("open")
  }
})
const exploreBtnEls = document.querySelectorAll(".explore-btn");
exploreBtnEls.forEach(exploreBtnEl => {
  exploreBtnEl.addEventListener("click", () => {
    scroll.animateScroll(document.querySelector("#about-us"))
  })
})

//鎶樺彔鎸夐挳
const burgerEl = document.querySelector(".burger")
burgerEl.addEventListener("click", () => {
  headerEL.classList.toggle("open")
})