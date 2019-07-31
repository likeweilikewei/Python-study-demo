"""
一、模拟吉他 要开发一个自动识别谱子的吉他模拟器，达到录入谱即可按照谱发声的效果。
除了发声设备外（假设已完成），最重要的就是读谱和译谱能力了。
分析其需求，整个过程大致上分可以分为两部分：根据规则翻译谱的内容；根据翻译的内容演奏。
我们用一个解释器模型来完成这个功能。 class PlayContext(): play_text = None class Express

要开发一个自动识别谱子的吉他模拟器，达到录入谱即可按照谱发声的效果。
除了发声设备外（假设已完成），最重要的就是读谱和译谱能力了。分析其需求，整个过程大致上分可以分为两部分：
根据规则翻译谱的内容；根据翻译的内容演奏。我们用一个解释器模型来完成这个功能。
"""


class PlayContext:
    play_text = None


class Expression:
    def interpret(self, context):
        if len(context.play_text) == 0:
            return
        else:
            play_segs=context.play_text.split(" ")
            for play_seg in play_segs:
                pos=0
                for ele in play_seg:
                    if ele.isalpha():
                        pos+=1
                        continue
                    break
                play_chord = play_seg[0:pos]
                play_value = play_seg[pos:]
                self.execute(play_chord,play_value)

    def execute(self,play_key,play_value):
        pass


class NormGuitar(Expression):
    def execute(self, key, value):
        print("Normal Guitar Playing--Chord:%s Play Tune:%s"%(key,value))


if __name__=="__main__":
    context = PlayContext()
    context.play_text = "C53231323 Em43231323 F43231323 G63231323"
    guitar=NormGuitar()
    guitar.interpret(context)
