<template>
<div style="color: #484848;">
  <b-navbar toggleable="lg">
    <b-navbar-brand href="#">
      <img src="https://placekitten.com/g/30/30" alt="Kitten">
    </b-navbar-brand>
     <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    

    <b-collapse id="nav-collapse" is-nav>
         <b-nav-form>
            <b-input-group prepend="@">
                <b-form-input placeholder="住宿" size="lg"></b-form-input>
            </b-input-group>
            <b-input-group-append>
                <b-button variant="info">搜尋</b-button>
            </b-input-group-append>
        </b-nav-form>


      <!-- Right aligned nav items -->

        <b-navbar-nav class="ml-auto">
            <b-nav-item href="#">成為房東</b-nav-item>
            <b-nav-item href="#">登入</b-nav-item>
            <b-nav-item href="#">註冊</b-nav-item>
        </b-navbar-nav>

    </b-collapse>
  </b-navbar>
</div>
</template>

<script>
export default {
    

}
</script>

<style lang="scss" scoped>
    b-navbar-nav{
        display:flex;
        justify-content:flex-end;
    }
    
</style>