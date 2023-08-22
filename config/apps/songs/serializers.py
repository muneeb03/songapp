from rest_framework import serializers
from apps.songs.models import Song, ScheduledSong, Album, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text']


class SongSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Song
        fields = ['id','title','artist','release_date', 'comments']


class ScheduledSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledSong
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'description', 'is_public', 'songs']


class AlbumCreateSerializer(serializers.ModelSerializer):
    songs = serializers.ListField(child=serializers.IntegerField())

    class Meta:
        model = Album
        fields = ['title', 'description', 'songs']

    def create(self, validated_data):
        songs_data = validated_data.pop('songs')
        album = Album.objects.create(**validated_data)
        for song_id in songs_data:
            song = Song.objects.get(id=song_id)
            album.songs.add(song)
        return album


class AlbumSongSerializer(serializers.Serializer):
    song_ids = serializers.ListField(child=serializers.IntegerField())


class AddSongsToAlbumSerializer(serializers.Serializer):
    song_ids = serializers.ListField(child=serializers.IntegerField())

