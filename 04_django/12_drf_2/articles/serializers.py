from rest_framework import serializers
from .models import Article, Comment

# 접근 제어자 
# private, protected, default, public 
#     String name

#     getName return 
#     setName void

# 단일 게시글 데이터(단일 인스턴스)를 직렬화 하는 도구
# 그러면 ArticleListSerializer를 단일 게시글에서는 못쓰나요? ==> NO
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
    
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content', )

    comment_set = CommentDetailSerializer(read_only=True, many=True)
    
    num_of_comments = serializers.SerializerMethodField()

    def get_num_of_comments(self, obj):
        return obj.num_of_comments

# 전체 게시글 데이터(쿼리셋)를 직렬화 하는 도구
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article')


    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title', ) 
        
    article = ArticleTitleSerializer(read_only=True)
    