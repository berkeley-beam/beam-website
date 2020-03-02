

  const data = [
    { dateLabel: 'January 2017', title: 'Gathering Information' },
    { dateLabel: 'February 2017', title: 'Planning' },
    { dateLabel: 'March 2017', title: 'Design' },
    { dateLabel: 'April 2017', title: 'Content Writing and Assembly' },
    { dateLabel: 'May 2017', title: 'Coding' },
    { dateLabel: 'June 2017', title: 'Testing, Review & Launch' },
    { dateLabel: 'July 2017', title: 'Maintenance' }
  ];

  new Vue({
    el: '#app',
    data: {
      steps: data,
    },
    mounted() {
      var swiper = new Swiper('.swiper-container', {
        pagination: '.swiper-pagination',
        slidesPerView: 4,
        paginationClickable: true,
        grabCursor: true,
        paginationClickable: true,
        nextButton: '.next-slide',
        prevButton: '.prev-slide',
      });
    }
  })