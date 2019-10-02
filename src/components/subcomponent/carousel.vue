<template>
  <div>
    <b-carousel
      id="carousel-1"
      v-model="slide"
      controls
      indicators
      background="#ababab"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >

      <b-carousel-slide img-src="https://a0.muscache.com/im/pictures/55113277/8e202e00_original.jpg?aki_policy=large"></b-carousel-slide>

      <b-carousel-slide img-src="https://a0.muscache.com/im/pictures/ef65a655-2397-473b-9aff-382c1447262f.jpg?aki_policy=large"></b-carousel-slide>

      <b-carousel-slide img-src="https://a0.muscache.com/im/pictures/5075af60-abe6-4f67-8b3a-8313c765867c.jpg?aki_policy=large"></b-carousel-slide>

 

    </b-carousel>

  </div>
</template>

<script>
  export default {
    data() {
      return {
        slide: 0,
        sliding: null
      }
    },
    methods: {
      onSlideStart(slide) {
        this.sliding = true
      },
      onSlideEnd(slide) {
        this.sliding = false
      },
     
    }
  }
</script>