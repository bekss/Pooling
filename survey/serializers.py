from rest_framework import serializers
from .models import Polls, Choices, Question, Answer


class User(object):
    def set_context(self, serializer_field):
        self.user = serializer_field.context['request'].user.id

    def __call__(self):
        return self.user


class AnswerSerializer(serializers.ModelSerializer):
    answer_id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(default=User)
    poll = serializers.SlugRelatedField(queryset=Polls.objects.all(), slug_field='id')
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    choice = serializers.SlugRelatedField(queryset=Choices.objects.all(), slug_field='id', allow_null=True)

    class Meta:
        model = Answer
        fields = '__all__'

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def validate(self, attrs):
        question = Question.objects.get(id=attrs['question'].id).type
        try:
            if question == 'one' or question == 'text':
                obj = Answer.objects.get(question=attrs['question'].id, poll=attrs['pol'], user=attrs['user'])
            elif question == 'multiple':
                obj = Answer.objects.get(question=attrs['question'].id, poll=attrs['poll'], user=attrs['user'],
                                         choice=attrs['choice'])
        except Answer.DoesNotExist:
            return attrs
        else:
            raise serializers.ValidationError('Have got')


class ChoiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    choice_text = serializers.CharField(max_length=200)

    def validate(self, attrs):
        try:
            obj = Choices.objects.get(question_choice=attrs['question'].id, choice_text=attrs['choice_text'])
        except Choices.DoesNotExist:
            return attrs
        else:
            raise serializers.ValidationError('Have got')

    class Meta:
        model = Choices
        fields = '__all__'

    def create(self, validated_data):
        return Choices.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    poll = serializers.SlugRelatedField(queryset=Polls.objects.all(), slug_field='id')
    question_text = serializers.CharField(max_length=200)
    question_type = serializers.CharField(max_length=200)
    choices = ChoiceSerializer(many=True, read_only=True)

    def validate(self, attrs):
        question_type = attrs['type']
        if question_type == 'one' or question_type == 'multiple' or question_type == 'text':
            return attrs
        raise serializers.ValidationError('Тип вопроса может быть только один или несколько или же текстовым')

    class Meta:
        model = Question
        fields = '__all__'

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class PollSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    date_start = serializers.DateTimeField()
    date_end = serializers.DateTimeField()
    description = serializers.CharField(max_length=200)
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Polls
        fields = '__all__'

    def create(self, validated_data):
        return Polls.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'pub_date' in validated_data:
            raise serializers.ValidationError({'date_start': 'Это поле не может быть изменен'})
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance