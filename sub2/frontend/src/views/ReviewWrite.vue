<template>
  <v-container grid-list-xl>
    <v-layout row justify-center align-center wrap class="mt-4 pt-2">
      <v-flex xs12 sm12 md6 lg6 xl6>
        <h2 class="pb-4 mb-0"><b>리뷰작성</b></h2>
        <h4><b>당신의 리뷰를 남겨주세요.</b></h4>
        <form>
      <!-- <v-text-field
        name="review.title"
        color="blue"
        background-color="transparent"
        v-model="review.title"
        label="제목"
        data-aos="fade-right"
      ></v-text-field> -->

      <v-textarea
        color="blue"
        background-color="transparent"
        :counter="200"
        v-model="review.contents"
        label="이 곳에 대하여 어떻게 생각하시나요?"
        name="body"
      ></v-textarea>

      <star-rating v-model="review.evaluate" v-bind:star-size="50"></star-rating>
    </form>
    <br>
          <v-btn @click="submit()" type="submit" color="primary" class="white--text"
            >등록하기</v-btn>

          <v-btn to="/infodetail">
          <v-icon>arrow_back</v-icon>취소하기
        </v-btn>
      </v-flex>
    </v-layout>
  </v-container>


</template>

<script>
import { mapGetters } from "vuex";
import StarRating from 'vue-star-rating'

export default {
  name: "TeamMain",
  computed: {
    ...mapGetters([
      "select_info",
      "select_detail"
    ]),
  },
  mounted() {

  },
  components: {
    StarRating

  },
  created() {
  },
  data() {
    return {
      review :{
        userid:"",
        title :"",
        contents :"",
        write_date:"",
        evaluate: 0,
      }
    };
  },

  methods: {
    submit(){
        if (this.review.contents == "") {
          alert('리뷰 내용을 작성해주세요')
        } else if (this.review.evaluate == 0) {
          alert('별점을 입력해주세요')
        } else {
          const data = {
            'Spok_pk' : this.select_detail.id,
            'data' : {
              'content': this.review.contents,
              'rating' : this.review.evaluate
            }
          }

          this.$store.dispatch("WRITE_REVIEW", data)
          .then(()=>{
            alert('리뷰작성 성공!')
            this.$router.push("/infodetail");
          })

        }

    }


  }
}
</script>

<style scoped>

</style>
