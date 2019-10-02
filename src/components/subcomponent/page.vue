<template>
  <div class="mt-3">
    <b-pagination-nav align="right" :link-gen="linkGen" size="lg" :number-of-pages="10" use-router></b-pagination-nav>
  </div>

</template>

<script>
  export default {
    methods: {
      linkGen(pageNum) {
        return pageNum === 1 ? '?' : `?page=${pageNum}`
      }
    }
  }
</script>